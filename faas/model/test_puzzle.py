
from .puzzle import puzzle_urn, Puzzle


def test_puzzle_urn_returns_correct_key():
    assert 'puzzle:mypuzzle' == puzzle_urn('mypuzzle')


def test_puzzle_can_contruct():
    p = Puzzle('name', 'desc', ['words'])
    assert p is not None


def test_puzzle_is_iterable():
    p = Puzzle('name', 'desc', ['words'])

    d = {'name': 'name', 'description': 'desc', 'words': ['words']}
    assert d == dict(p)
