
from ..handler_models import Request, Response
from ..models.puzzle import set_puzzle, Puzzle


class HuntwordsPuzzleUpdatedCommand(object):
    """Command class that processes puzzle-updated message"""

    def run(self, request: Request):
        """Command that processes puzzle-updated message"""

        obj = request.body
        puzzle = Puzzle(obj["name"], obj["description"], obj["words"])
        jpuzzle = dict(puzzle)

        set_puzzle(puzzle.name, puzzle)

        return Response(200, jpuzzle, {})
