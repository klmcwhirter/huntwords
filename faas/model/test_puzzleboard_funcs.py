import pytest

from .puzzleboard import direction_hints, is_direction, Point, WordSolution, word_points


@pytest.mark.parametrize('direction_hint', direction_hints.keys())
def test_is_direction_return_false_if_no_solution(direction_hint: str):
    ws = WordSolution('word')
    pred = is_direction(direction_hint)
    assert not pred(ws)


@pytest.mark.parametrize('direction_hint,direction', [(h, d) for (h, ds) in direction_hints.items() for d in ds])
def test_is_direction_return_True_if_vertical(direction_hint, direction):
    ws = WordSolution('word', placed=True, direction=direction)
    pred = is_direction(direction_hint)
    assert pred(ws)


@pytest.mark.parametrize('origin, direction, expected', [
    # Left to right and/or down
    (Point(0, 0), 'E', [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]),
    (Point(0, 0), 'SE', [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]),
    (Point(0, 0), 'S', [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]),

    # Right to left and/or up
    (Point(4, 4), 'SW', [Point(4, 4), Point(3, 5), Point(2, 6), Point(1, 7)]),
    (Point(4, 4), 'W', [Point(4, 4), Point(3, 4), Point(2, 4), Point(1, 4)]),
    (Point(4, 4), 'NW', [Point(4, 4), Point(3, 3), Point(2, 2), Point(1, 1)]),
    (Point(4, 4), 'N', [Point(4, 4), Point(4, 3), Point(4, 2), Point(4, 1)]),
    (Point(4, 4), 'NE', [Point(4, 4), Point(5, 3), Point(6, 2), Point(7, 1)]),
])
def test_word_points_per_direction(origin: Point, direction: str, expected: list[Point]):
    word = 'WORD'
    points = word_points(word, origin, direction)

    assert expected == points
