''' models for the puzzleboard concept '''

from .redis import redis_client


def puzzleboard_urn(name):
    ''' redis universal resource name '''
    return f'urn:puzzleboard:{name}'


class PuzzleBoard:
    def __init__(self, height, width, letters, solutions, puzzle):
        self.height = height
        self.width = width
        self.letters = letters
        self.solutions = solutions
        self.puzzle = puzzle

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'height', self.height
        yield 'width', self.width
        yield 'letters', self.letters
        yield 'solutions', self.solutions
        yield 'puzzle', dict(self.puzzle)


def push_puzzleboard(name, pboard):
    r = redis_client()
    r.rpush(puzzleboard_urn(name), pboard)
