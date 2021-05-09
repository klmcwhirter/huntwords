import json

from .handler_models import Event, Response
from .model.puzzle import set_puzzle, Puzzle


class HuntwordsPuzzleUpdatedCommand(object):
    """Command class that processes puzzle-updated message"""

    def run(self, event: Event, context):
        """Command that processes puzzle-updated message"""

        obj = json.loads(event.request.body)
        puzzle = Puzzle(obj["name"], obj["description"], obj["words"])
        jpuzzle = json.dumps(dict(puzzle))

        set_puzzle(puzzle.name, puzzle)

        return Response(200, jpuzzle, {})
