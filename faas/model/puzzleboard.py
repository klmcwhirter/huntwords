''' models for the puzzleboard concept '''
import random
import string

from .puzzle import Puzzle
from .redis import redis_client


def puzzleboard_urn(name):
    ''' redis universal resource name '''
    return f'puzzleboard:{name}'


def push_puzzleboard(name, pboard):
    '''Place the board in the cache for usage'''
    r = redis_client()
    r.rpush(puzzleboard_urn(name), pboard)


config = {
    'retries': 2048,
    'diagonal_ratio': 0.095,
    'random_factor': 32,
    'word_density': 0.6
}


class Point:
    '''Represents a cell on the puzzle board'''

    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'X', self.X
        yield 'Y', self.Y


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

direction_hints: dict[str, str] = {
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
    for i, ch in enumerate(list(word)):
        points.append(Point(origin.X, origin.Y))
        origin.X += offsets.X
        origin.Y += offsets.Y
    return points


class WordSolution:
    def __init__(self, word, placed=False, origin: Point = Point(0, 0), direction=None, points: list[Point] = None):
        self.word = word
        self.placed = placed
        self.origin = origin
        self.direction = direction
        if points is None:
            points = []
        self.points = points

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'word', self.word
        yield 'placed', self.placed
        yield 'origin', dict(self.origin)
        yield 'direction', self.direction
        yield 'points', [dict(p) for p in self.points]

    def __lt__(self, other):
        '''Supports sorting by word'''
        return self.word < other.word


class PuzzleBoard:
    def __init__(self,
                 height: int, width: int,
                 letters: list[str] = None,
                 solutions: list[WordSolution] = None,
                 puzzle: Puzzle = None):
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

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'height', self.height
        yield 'width', self.width
        yield 'letters', self.letters
        yield 'solutions', [dict(s) for s in self.solutions]
        yield 'puzzle', dict(self.puzzle)

    def fill_with_random_letters(self):
        '''Fills all empty cells on the board with random upper case letters'''
        for y in range(self.height):
            for x in range(self.width):
                if self.letters[y][x] is None:
                    self.letters[y][x] = random.choice(string.ascii_uppercase)

    def has_density(self):
        ''' Count of placed word letters / total grid letter count >= config['word_density'] '''
        word_letters = sum([len(sol.word) for sol in self.solutions])
        total = self.height * self.width
        return word_letters / total >= config['word_density']

    def is_full(self):
        '''Tests if all the cells of the board are full'''
        return not any([cell is None for row in self.letters for cell in row])

    def place(self, solution):
        ''' Commit the solution to the board '''
        for letter, point in zip(solution.word, solution.points):
            self.letters[point.Y][point.X] = letter

        self.solutions.append(solution)

    def placed_all_words(self):
        placed_words = set(sorted([sol.word for sol in self.solutions]))
        words = set(self.puzzle.words)
        return placed_words == words

    def try_letter_solution(self, letter: str, point: Point) -> bool:
        '''Tests if a letter can be placed in the location requested'''

        # make sure point is in the grid
        value = ''
        if point.X >= 0 and point.X < self.width and point.Y >= 0 and point.Y < self.height:
            value = self.letters[point.Y][point.X]

        return value is None or value == letter

    def try_place_word(self, word, origin, direction):
        '''tests if word can be placed on the board, and if so returns WordSolution'''
        solution = None

        if not self.is_full():
            points = word_points(word, origin, direction)

            if all([self.try_letter_solution(letter, point) for letter, point in zip(word, points)]):
                solution = WordSolution(word=word,
                                        placed=True,
                                        origin=origin,
                                        direction=direction,
                                        points=points)

        return solution

    def valid(self):
        '''Validates the quality of the generated board'''

        rc = False

        # must have at least config['diagonal_ratio'] diagonal solutions
        if len(self.solutions) > 0:
            rc = len(list(filter(is_direction('diagonal'), self.solutions))) / len(self.solutions) >= config['diagonal_ratio']

        # must have at least one vertical solution
        rc &= len(list(filter(is_direction('vertical'), self.solutions))) >= 1

        # must have at least one horizontal solution
        rc &= len(list(filter(is_direction('horizontal'), self.solutions))) >= 1

        # If there are not enough words in the puzzle to fulfill the requirements, and all were placed - accept it
        rc |= self.placed_all_words()

        return rc

    def words_to_place(self):
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


def generate_puzzleboard(height, width, puzzle):
    '''Generate a puzzleboard for the puzzle and dimensions passed'''
    maxtries = len(direction_offsets.keys()) * width * height * config['random_factor']

    for retry in range(config['retries']):
        # initialize an instance
        pboard = PuzzleBoard(height, width, puzzle=puzzle)
        assert not pboard.is_full()

        for word in pboard.words_to_place():
            for curr_try in range(maxtries):
                origin = Point(random.randint(0, pboard.width), random.randint(0, pboard.height))
                direction = random.choice(list(direction_offsets.keys()))

                solution = pboard.try_place_word(word, origin, direction)
                if solution:
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
