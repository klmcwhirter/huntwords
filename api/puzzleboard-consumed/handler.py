'''Handles a request for the huntwords.puzzle.consumed message'''

from .puzzleboard_consumed import HuntwordsPuzzleBoardComsumedCommand


def handle(req):
    '''handle a request to the function
    Args:
        req (str): request body
    '''
    resp = HuntwordsPuzzleBoardComsumedCommand().run(req)
    return resp
