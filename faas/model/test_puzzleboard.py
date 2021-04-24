from itertools import islice

import pytest

from .puzzle import Puzzle
from .puzzleboard import is_direction, puzzleboard_urn, Point, PuzzleBoard, WordSolution


def test_puzzleboard_urn_returns_correct_key():
    assert 'puzzleboard:mypuzzle' == puzzleboard_urn('mypuzzle')


@pytest.fixture
def test_puzzle():
    return Puzzle('test_puzzle', '', ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])


@pytest.fixture
def test_puzzleboard(test_puzzle):
    return PuzzleBoard(10, 10, puzzle=test_puzzle)


def test_puzzleboard_can_contruct_with_defaults():
    height = 14
    width = 15

    p = PuzzleBoard(height, width)
    assert p is not None

    assert p.letters is not None

    # count of rows in p.letters per height param above
    assert height == len(p.letters)

    # count of cells per row in p.letters per width param above
    assert all([width == len(r) for r in p.letters])

    # All cells should be None by default
    assert all([cell is None for row in p.letters for cell in row])

    assert p.solutions is not None

    # if no puzzle is provided ...
    assert p.puzzle is None


def test_puzzleboard_can_contruct_with_letters():
    height = 14
    width = 15
    letters = [['X'] * width] * height

    p = PuzzleBoard(height, width, letters=letters)
    assert p is not None

    assert p.letters is not None

    # should be same instance of letters passed in
    assert p.letters is letters

    # All cells should have 'X'
    assert all([cell == 'X' for row in p.letters for cell in row])


def test_fill_with_random_letters_replaces_all_None(test_puzzleboard):
    test_puzzleboard.fill_with_random_letters()
    assert all([cell is not None for row in test_puzzleboard.letters for cell in row])


def test_fill_with_random_letters_does_not_touch_placed_letters(test_puzzleboard):

    test_puzzleboard.letters[3][3] = 'z'
    test_puzzleboard.letters[5][5] = 'n'
    test_puzzleboard.letters[8][8] = 'l'

    # some, but not all placed
    assert not all([cell is not None for row in test_puzzleboard.letters for cell in row])

    test_puzzleboard.fill_with_random_letters()

    assert all([cell is not None for row in test_puzzleboard.letters for cell in row])

    assert 'z' == test_puzzleboard.letters[3][3]
    assert 'n' == test_puzzleboard.letters[5][5]
    assert 'l' == test_puzzleboard.letters[8][8]


def test_has_density_is_False_if_no_solutions(test_puzzleboard):
    assert not test_puzzleboard.has_density()


def test_has_density_is_False_if_just_shy(test_puzzleboard):
    ''' Note: word letter count / total grid letter count >= 0.6
    10x10 == 100
    100 * 0.6 = 60 - so 59 should give False
    '''
    test_puzzleboard.solutions = [WordSolution('X' * 59)]
    assert not test_puzzleboard.has_density()


def test_has_density_is_False_if_just_shy_as_sum(test_puzzleboard):
    ''' Note: word letter count / total grid letter count >= 0.6
    10x10 == 100
    100 * 0.6 = 60 - so 59 should give False
    '''
    test_puzzleboard.solutions = [
        WordSolution('X' * 20),
        WordSolution('X' * 20),
        WordSolution('X' * 19)
    ]
    assert not test_puzzleboard.has_density()


def test_has_density_is_True_if_equal(test_puzzleboard):
    ''' Note: word letter count / total grid letter count >= 0.6
    10x10 == 100
    100 * 0.6 = 60 - so 60 should give True
    '''
    test_puzzleboard.solutions = [WordSolution('X' * 60)]
    assert test_puzzleboard.has_density()


def test_has_density_is_True_if_equal_as_sum(test_puzzleboard):
    ''' Note: word letter count / total grid letter count >= 0.6
    10x10 == 100
    100 * 0.6 = 60 - so 60 should give True
    '''
    test_puzzleboard.solutions = [
        WordSolution('X' * 15),
        WordSolution('X' * 25),
        WordSolution('X' * 20)
    ]
    assert test_puzzleboard.has_density()


def test_is_full_false_when_no_letters_placed(test_puzzleboard):
    assert not test_puzzleboard.is_full()


def test_puzzleboard_is_iterable(test_puzzleboard):
    d = {'height': 10, 'width': 10, 'letters': [], 'solutions': [], 'puzzle': dict(test_puzzleboard.puzzle)}
    test_puzzleboard.letters = []

    # can leverage iterabiity with dict protocol
    assert d == dict(test_puzzleboard)


def test_try_letter_solution_true_if_None(test_puzzleboard):
    assert test_puzzleboard.try_letter_solution('W', Point(0, 0))


def test_try_letter_solution_false_if_filled(test_puzzleboard):
    test_puzzleboard.letters[0][0] = 'F'
    assert not test_puzzleboard.try_letter_solution('W', Point(0, 0))


def test_try_letter_solution_false_if_outside_of_grid(test_puzzleboard):
    assert not test_puzzleboard.try_letter_solution('W', Point(-1, -2))


def test_try_letter_solution_true_if_overlap(test_puzzleboard):
    test_puzzleboard.letters[0][0] = 'W'
    assert test_puzzleboard.try_letter_solution('W', Point(0, 0))


def test_try_place_word_returns_solution_on_empty_board(test_puzzleboard):
    solution = test_puzzleboard.try_place_word('WORD', Point(0, 0), 'E')
    assert solution is not None


def test_try_place_word_returns_solution_if_at_least_one_overlap(test_puzzleboard):
    test_puzzleboard.letters[0][0] = 'W'
    solution = test_puzzleboard.try_place_word('WORD', Point(0, 0), 'E')
    assert solution is not None
    assert solution.placed
    assert [Point(x, 0) for x in range(4)] == solution.points
    assert 'WORD' == solution.word


def test_try_place_word_returns_solution_if_3_overlap(test_puzzleboard):
    test_puzzleboard.letters[0][0] = 'W'
    test_puzzleboard.letters[2][0] = 'R'
    test_puzzleboard.letters[3][0] = 'D'
    solution = test_puzzleboard.try_place_word('WORD', Point(0, 0), 'E')
    assert solution is not None
    assert solution.placed
    assert [Point(x, 0) for x in range(4)] == solution.points
    assert 'WORD' == solution.word


def test_try_place_word_returns_solution_if_full_but_one_slot(test_puzzleboard):
    test_puzzleboard.fill_with_random_letters()
    test_puzzleboard.letters[3][3] = 'W'
    test_puzzleboard.letters[4][4] = None
    test_puzzleboard.letters[5][5] = None
    test_puzzleboard.letters[6][6] = 'D'
    solution = test_puzzleboard.try_place_word('WORD', Point(3, 3), 'SE')
    assert solution is not None
    assert solution.placed
    assert [Point(x, x) for x in range(3, 7)] == solution.points
    assert 'WORD' == solution.word


def test_try_place_word_returns_None_on_full_board(test_puzzleboard):
    # simulate full board
    test_puzzleboard.fill_with_random_letters()

    solution = test_puzzleboard.try_place_word('WORD', Point(0, 0), 'E')
    assert solution is None


def test_try_place_word_returns_None_when_cannot_place_word(test_puzzleboard):
    # simulate position occupied
    for i, ch in enumerate(list('OTHER')):
        test_puzzleboard.letters[0][i] = ch

    solution = test_puzzleboard.try_place_word('WORD', Point(0, 0), 'E')
    assert solution is None


def test_valid_is_false_if_no_solutions(test_puzzleboard):
    assert not test_puzzleboard.valid()


def test_valid_is_true_if_criteria_met(test_puzzleboard):
    word = 'word'
    test_puzzleboard.solutions = [
        WordSolution(word, placed=True, direction='N'),  # vertical
        WordSolution(word, placed=True, direction='S'),  # vertical
        WordSolution(word, placed=True, direction='N'),  # vertical
        WordSolution(word, placed=True, direction='S'),  # vertical
        WordSolution(word, placed=True, direction='W'),  # horizontal
        WordSolution(word, placed=True, direction='E'),  # horizontal
        WordSolution(word, placed=True, direction='W'),  # horizontal
        WordSolution(word, placed=True, direction='E'),  # horizontal
        WordSolution(word, placed=True, direction='NW')  # diagonal
    ]
    assert 9 == len(test_puzzleboard.solutions)
    assert 4 == len(list(filter(is_direction('vertical'), test_puzzleboard.solutions)))
    assert 4 == len(list(filter(is_direction('horizontal'), test_puzzleboard.solutions)))
    assert 1 == len(list(filter(is_direction('diagonal'), test_puzzleboard.solutions)))
    assert test_puzzleboard.valid()


def test_valid_is_false_if_criteria_not_met(test_puzzleboard):
    word = 'word'
    test_puzzleboard.solutions = [
        WordSolution(word, placed=True, direction='N'),  # vertical
        WordSolution(word, placed=True, direction='S'),  # vertical
        WordSolution(word, placed=True, direction='N'),  # vertical
        WordSolution(word, placed=True, direction='S'),  # vertical
        WordSolution(word, placed=True, direction='W'),  # horizontal
        WordSolution(word, placed=True, direction='E'),  # horizontal
        WordSolution(word, placed=True, direction='W'),  # horizontal
        WordSolution(word, placed=True, direction='E'),  # horizontal
        WordSolution(word, placed=True, direction='W'),  # horizontal
        WordSolution(word, placed=True, direction='E'),  # horizontal
        WordSolution(word, placed=True, direction='NW')  # diagonal
    ]
    assert 11 == len(test_puzzleboard.solutions)
    assert 4 == len(list(filter(is_direction('vertical'), test_puzzleboard.solutions)))
    assert 6 == len(list(filter(is_direction('horizontal'), test_puzzleboard.solutions)))
    assert 1 == len(list(filter(is_direction('diagonal'), test_puzzleboard.solutions)))
    assert not test_puzzleboard.valid()


@pytest.mark.parametrize('list_size', [3, 10, 25])
def test_words_to_place_returns_n_words(list_size, test_puzzleboard):
    words_to_place = [word for word in islice(test_puzzleboard.words_to_place(), list_size)]
    assert list_size == len(words_to_place)


@pytest.mark.parametrize('n', range(10))
def test_words_to_place_returns_random_word_lists(n, test_puzzleboard):
    list_size = 30
    words_to_place1 = [word for word in islice(test_puzzleboard.words_to_place(), list_size)]
    words_to_place2 = [word for word in islice(test_puzzleboard.words_to_place(), list_size)]

    assert words_to_place1 != words_to_place2
