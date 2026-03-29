
from api.models.command import CommandRequest, CommandResponse
from api.models.puzzle import Puzzle, set_puzzle


class HuntwordsPuzzleUpdatedCommand(object):
    """Command class that processes puzzle-updated message"""

    def run(self, request: CommandRequest):
        """Command that processes puzzle-updated message"""

        obj = request.body
        puzzle = Puzzle(obj["name"], obj["description"], obj["pb_count"], obj["words"])
        jpuzzle = dict(puzzle)

        set_puzzle(puzzle.name, puzzle)

        return CommandResponse(200, jpuzzle, {})
