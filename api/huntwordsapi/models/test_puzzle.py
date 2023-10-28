
from .puzzle import puzzle_urn, Puzzle, get_puzzle
from redis import Redis


def test_puzzle_urn_returns_correct_key():
    assert 'puzzle:mypuzzle' == puzzle_urn('mypuzzle')


def test_puzzle_can_contruct():
    p = Puzzle('name', 'desc', ['WORDS'])
    assert p is not None


def test_puzzle_is_iterable():
    p = Puzzle('name', 'desc', ['WORDS'])

    d = {'name': 'name', 'description': 'desc', 'words': ['WORDS']}
    assert d == dict(p)


def test_get_puzzle_(monkeypatch):
    jsonstr = '''{
        "name": "test",
        "description": "test",
        "words": []
    }'''
    monkeypatch.setattr(Redis, '__init__', lambda *args, **kwargs: None)
    monkeypatch.setattr(Redis, 'get', lambda *args, **kwargs: jsonstr)
    monkeypatch.setattr(Redis, 'close', lambda *args, **kwargs: jsonstr)

    rc = get_puzzle('test')

    assert rc is not None
    assert 'test' == rc.name
