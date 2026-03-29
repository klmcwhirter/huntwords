
from api.models.command import CommandRequest, CommandResponse
from api.models.puzzle import get_puzzles


class HuntwordsPuzzlesCommand(object):
    """Command class that processes puzzles message"""

    def run(self, request: CommandRequest) -> CommandResponse:
        """Command that processes puzzles message"""

        puzzles = get_puzzles()

        return CommandResponse(200, puzzles, {})
