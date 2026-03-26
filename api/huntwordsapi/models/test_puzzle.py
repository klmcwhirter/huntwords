

from unittest.mock import Mock

import huntwordsapi.models.repo
from huntwordsapi.models.puzzle import Puzzle, get_puzzle
from huntwordsapi.models.repo import PuzzleRepo


def test_puzzle_can_contruct():
    p = Puzzle('name', 'desc', ['WORDS'])
    assert p is not None


def test_puzzle_is_iterable():
    p = Puzzle('name', 'desc', ['WORDS'])

    d = {'name': 'name', 'description': 'desc', 'words': ['WORDS']}
    assert d == dict(p)


def test_get_puzzle_by_name(monkeypatch):
    with monkeypatch.context() as m:
        jsonstr: str = '''{
            "name": "test",
            "description": "test",
            "words": []
        }'''
        mock_repo = Mock(spec=PuzzleRepo)
        mock_repo.puzzle_by_name.return_value = jsonstr

        m.setattr(huntwordsapi.models.repo, '_pr_instance', mock_repo)

        rc = get_puzzle('test')

    assert rc is not None
    assert 'test' == rc.name
