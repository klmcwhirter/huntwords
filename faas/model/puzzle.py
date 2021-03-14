''' models for the puzzle concept '''
import json

from .redis import redis_client


def puzzle_urn(name):
    ''' redis universal resource name '''
    return f'urn:puzzle:{name}'


class Puzzle:
    def __init__(self, name, description, words):
        self.name = name
        self.description = description
        self.words = words

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'name', self.name
        yield 'description', self.description
        yield 'words', self.words


def get_puzzle(name):
    r = redis_client()
    jtext = r.get(puzzle_urn(name))

    obj = json.loads(jtext)
    puzzle = Puzzle(obj['name'], obj['description'], obj['words'])

    return puzzle


def set_puzzle(name, puzzle):
    r = redis_client()
    r.set(puzzle_urn(name), puzzle)
