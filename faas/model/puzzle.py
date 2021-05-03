''' models for the puzzle concept '''
import json

from .redis import redis_client


def puzzle_urn(name) -> str:
    ''' redis universal resource name '''
    return f'puzzle:{name}'


class Puzzle:
    def __init__(self, name, description, words):
        self.name = name
        self.description = description
        self.words = [word.upper() for word in words]

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'name', self.name
        yield 'description', self.description
        yield 'words', self.words


def puzzle_from_dict(d: dict) -> Puzzle:
    return Puzzle(
        d['name'],
        d['description'],
        d['words']
    )


def get_puzzle(name: str) -> Puzzle:
    r = redis_client()
    jtext = r.get(puzzle_urn(name))

    obj = json.loads(jtext)
    puzzle = Puzzle(obj['name'], obj['description'], obj['words'])

    return puzzle


def set_puzzle(name: str, puzzle: Puzzle):
    r = redis_client()
    r.set(puzzle_urn(name), json.dumps(dict(puzzle)))
