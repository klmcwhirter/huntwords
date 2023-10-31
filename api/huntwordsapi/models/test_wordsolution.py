from .puzzleboard import Point, WordSolution


def test_wordsolution_can_construct():
    ws = WordSolution('WORD')
    assert ws is not None


def test_wordsolution_is_iterable():
    d = {'word': 'WORD', 'placed': False, 'origin': {'x': 0, 'y': 0}, 'direction': None, 'points': []}
    ws = WordSolution('WORD')

    # can leverage iterabiity with dict protocol
    assert d == dict(ws)


def test_wordsolution_overlaps_detects_intersection():
    ws = WordSolution('APPLE')
    ws.points = [Point(x, x) for x in range(4, 5+4)]

    paws = WordSolution('PINEAPPLE')
    paws.points = [Point(x, x) for x in range(9)]

    assert ws.overlaps([paws])


def test_wordsolution_overlaps_detects_no_intersection():
    points = [Point(x, x) for x in range(5)]

    ws = WordSolution('APPLE')
    ws.points = [Point(x, x+2) for x in range(4, 5+4)]

    paws = WordSolution('PINEAPPLE')
    paws.points = [Point(x, x) for x in range(9)]

    assert not ws.overlaps([paws])
