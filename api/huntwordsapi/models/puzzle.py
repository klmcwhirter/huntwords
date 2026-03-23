''' models for the puzzle concept '''
import json
from typing import Self

from .repo import puzzle_repo

class Puzzle:
    def __init__(self: Self, name: str, description: str, words: list[str]):
        self.name = name
        self.description = description
        self.words = [word.upper() for word in words]

    def __iter__(self: Self):
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
    r = puzzle_repo()
    jtext = r.puzzles.get(name, '')

    obj = json.loads(jtext)
    puzzle = Puzzle(obj['name'], obj['description'], obj['words'])

    return puzzle


def get_puzzles() -> list[Puzzle]:
    r = puzzle_repo()

    puzzles = [get_puzzle(name) for name in r.puzzles]
    return puzzles


def set_puzzle(name: str, puzzle: Puzzle) -> None:
    r = puzzle_repo()
    r.puzzles[name] = json.dumps(dict(puzzle))
