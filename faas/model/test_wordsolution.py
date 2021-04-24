from .puzzleboard import WordSolution


def test_wordsolution_can_construct():
    ws = WordSolution('WORD')
    assert ws is not None


def test_wordsolution_is_iterable():
    d = {'word': 'WORD', 'placed': False, 'origin': {'X': 0, 'Y': 0}, 'direction': None, 'points': []}
    ws = WordSolution('WORD')

    # can leverage iterabiity with dict protocol
    assert d == dict(ws)
