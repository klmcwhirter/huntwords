'''Handles a request for the huntwords.puzzle.pop message'''

from .puzzleboard_pop import HuntwordsPuzzleBoardPopCommand


def handle(req):
    '''handle a request to the function
    Args:
        req (str): request body
    '''
    resp = HuntwordsPuzzleBoardPopCommand().run(req)
    return resp
