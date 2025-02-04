''' models for the puzzleboard concept '''
import json
import random
import string
from typing import Generator, Optional, Self

from .puzzle import Puzzle, puzzle_from_dict
from .redis import redis_client

config = {
    'retries': 2048,
    'diagonal_ratio': 0.098,
    'random_factor': 32,
    'word_density': 0.75
}


class Point:
    '''Represents a cell on the puzzle board'''

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'x', self.x
        yield 'y', self.y

    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'


def point_from_dict(d: dict) -> Point:
    return Point(d['x'], d['y'])


direction_offsets: dict[str, Point] = {
    'NW': Point(-1, -1),
    'N': Point(0, -1),
    'NE': Point(1, -1),
    'E': Point(1,  0),
    'SE': Point(1,  1),
    'S': Point(0,  1),
    'SW': Point(-1,  1),
    'W': Point(-1,  0)
}

direction_hints: dict[str, list[str]] = {
    'vertical': ['N', 'S'],
    'horizontal': ['E', 'W'],
    'diagonal': ['NW', 'NE', 'SE', 'SW']
}


def is_direction(direction_hint: str):
    '''Returns a function that tests a solution for a direction_hint'''
    def inner(s: WordSolution):
        '''Tests a WordSolution for being in a direction_hint'''
        return s.placed and s.direction in direction_hints[direction_hint]
    return inner


def word_points(word: str, origin: Point, direction: str) -> list[Point]:
    '''Given a word, a direction and point of placement, return the points on the board involved'''
    offsets = direction_offsets[direction]
    points = []
    for _ in range(len(word)):
        points.append(Point(origin.x, origin.y))
        origin.x += offsets.x
        origin.y += offsets.y
    return points


class WordSolution:
    def __init__(self: Self, word, placed=False, origin: Point = Point(0, 0), direction=None, points: Optional[list[Point]] = None):
        self.word = word
        self.placed = placed
        self.origin = origin
        self.direction = direction
        if points is None:
            points = []
        self.points = points

    def __iter__(self: Self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'word', self.word
        yield 'placed', self.placed
        yield 'origin', dict(self.origin)
        yield 'direction', self.direction
        yield 'points', [dict(p) for p in self.points]

    def __lt__(self: Self, other: Self):
        '''Supports sorting by word'''
        return self.word < other.word

    def __repr__(self: Self) -> str:
        return f'''WordSolution(
        word=\'{self.word}\',
        placed={self.placed},
        origin={self.origin},
        direction={self.direction},
        points={self.points})'''

    def overlaps(self: Self, solutions: list[Self]) -> bool:
        '''Detects whether this proposed solution overlaps completely with sny other - say APPLE and PINEAPPLE'''
        points_set = set(self.points)

        rc = False
        for ws in solutions:
            sol_points_set = set(ws.points)
            rc = len(points_set.intersection(sol_points_set)) == len(points_set)
            if rc:
                break
        return rc


def wordsolution_from_dict(d: dict) -> WordSolution:
    return WordSolution(
        d['word'],
        d['placed'],
        point_from_dict(d['origin']),
        d['direction'],
        [point_from_dict(p) for p in d['points']]
    )


class PuzzleBoard:
    def __init__(self: Self,
                 height: int, width: int,
                 letters: Optional[list[list[Optional[str]]]] = None,
                 solutions: Optional[list[WordSolution]] = None,
                 puzzle: Optional[Puzzle] = None):
        self.height = height
        self.width = width

        if letters is None:
            # don't use * to build up all dimensions - see:
            # https://docs.python.org/3/faq/programming.html#how-do-i-create-a-multidimensional-list
            letters = [[None] * self.width for r in range(self.height)]
        self.letters = letters

        if solutions is None:
            solutions = []
        self.solutions = solutions

        self.puzzle = puzzle

    def __iter__(self: Self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'height', self.height
        yield 'width', self.width
        yield 'letters', self.letters
        yield 'solutions', [dict(s) for s in self.solutions]
        yield 'puzzle', dict(self.puzzle) if self.puzzle else dict()

    def fill_with_random_letters(self: Self):
        '''Fills all empty cells on the board with random upper case letters'''
        for y in range(self.height):
            for x in range(self.width):
                if self.letters[y][x] is None:
                    self.letters[y][x] = random.choice(string.ascii_uppercase)

    def has_density(self: Self) -> float:
        ''' Count of placed word letters / total grid letter count >= config['word_density'] '''
        word_letters = sum([len(sol.word) for sol in self.solutions])
        total = self.height * self.width
        return word_letters / total >= config['word_density']

    def is_full(self: Self):
        '''Tests if all the cells of the board are full'''
        return all(cell is not None for row in self.letters for cell in row)

    def place(self: Self, solution: WordSolution):
        ''' Commit the solution to the board '''
        for letter, point in zip(solution.word, solution.points):
            self.letters[point.y][point.x] = letter

        self.solutions.append(solution)

    def placed_all_words(self: Self) -> bool:
        placed_words = set(sol.word for sol in self.solutions)
        words = set(self.puzzle.words) if self.puzzle else set()
        return placed_words == words

    def try_letter_solution(self: Self, letter: str, point: Point) -> bool:
        '''Tests if a letter can be placed in the location requested'''

        # make sure point is in the grid
        value = ''
        if point.x >= 0 and point.x < self.width and point.y >= 0 and point.y < self.height:
            value = self.letters[point.y][point.x]

        return value is None or value == letter

    def try_place_word(self: Self, word: str, origin: Point, direction: str) -> Optional[WordSolution]:
        '''tests if word can be placed on the board, and if so returns WordSolution'''
        solution = None

        if not self.is_full():
            points = word_points(word, origin, direction)

            if all(self.try_letter_solution(letter, point) for letter, point in zip(word, points)):
                solution = WordSolution(word=word,
                                        placed=True,
                                        origin=origin,
                                        direction=direction,
                                        points=points)

        return solution

    def valid(self: Self):
        '''Validates the quality of the generated board'''

        rc = False

        # must have at least config['diagonal_ratio'] diagonal solutions
        if len(self.solutions) > 0:
            rc = len(list(filter(is_direction('diagonal'), self.solutions))) / len(self.solutions) >= config['diagonal_ratio']

        if rc:
            # must have at least one vertical solution
            rc &= len(list(filter(is_direction('vertical'), self.solutions))) >= 1

        if rc:
            # must have at least one horizontal solution
            rc &= len(list(filter(is_direction('horizontal'), self.solutions))) >= 1

        # If there are not enough words in the puzzle to fulfill the requirements, and all were placed - accept it
        rc |= self.placed_all_words()

        return rc

    def words_to_place(self: Self) -> Generator[str, None, None]:
        '''Generator providing words from the puzzle'''
        words_set = set(self.puzzle.words)
        seen = set()
        while True:
            word = random.choice(self.puzzle.words)

            if word not in seen:
                seen.add(word)
                yield word

            if words_set == seen:
                break


def generate_puzzleboard(height: int, width: int, puzzle: Puzzle) -> PuzzleBoard:
    '''Generate a puzzleboard for the puzzle and dimensions passed'''
    max_tries = len(direction_offsets.keys()) * width * height * config['random_factor']

    pboard: PuzzleBoard  # = PuzzleBoard(height, width, puzzle=puzzle)

    for _ in range(config['retries']):
        # initialize an instance
        pboard = PuzzleBoard(height, width, puzzle=puzzle)
        assert not pboard.is_full()

        for word in pboard.words_to_place():
            for _ in range(max_tries):
                origin = Point(random.randint(0, pboard.width), random.randint(0, pboard.height))
                direction = random.choice(list(direction_offsets.keys()))

                solution = pboard.try_place_word(word, origin, direction)
                # if solution:
                if solution and not solution.overlaps(pboard.solutions):
                    pboard.place(solution)
                    break

            # do not need any more words
            if pboard.has_density():
                break

        pboard.solutions.sort()

        # board quality check
        if pboard.valid():
            # fill rest of board with random letters
            pboard.fill_with_random_letters()
            break

    return pboard


def puzzleboard_from_json(j: str) -> PuzzleBoard:
    pbdict = json.loads(j)
    return PuzzleBoard(
        pbdict['height'],
        pbdict['width'],
        pbdict['letters'],
        [wordsolution_from_dict(ws) for ws in pbdict['solutions']],
        puzzle_from_dict(pbdict['puzzle'])
    )


def puzzleboard_urn(name: str) -> str:
    ''' redis universal resource name '''
    return f'puzzleboard:{name}'


def clear_puzzleboards() -> None:
    '''Delete all puzzleboard lists'''
    r = redis_client()
    keys = r.keys(puzzleboard_urn('*'))
    r.delete(*keys)


def count_puzzleboard(name: str) -> int:
    '''Delete all puzzleboard lists'''
    r = redis_client()
    llen = r.llen(puzzleboard_urn(name))
    return llen


def pop_puzzleboard(name: str) -> PuzzleBoard:
    '''Pop a board from the cache; signal consumption'''
    r = redis_client()
    jpboard = r.lpop(puzzleboard_urn(name))
    return puzzleboard_from_json(jpboard)


def push_puzzleboard(name: str, pboard: PuzzleBoard):
    '''Place the board in the cache for usage'''
    r = redis_client()
    r.rpush(puzzleboard_urn(name), json.dumps(dict(pboard)))
