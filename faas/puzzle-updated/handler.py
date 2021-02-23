from .puzzle_updated import HuntwordsPuzzleUpdatedCommand


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    resp = HuntwordsPuzzleUpdatedCommand().run(req)
    return resp
