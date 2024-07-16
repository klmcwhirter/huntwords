
from ..models.command import CommandRequest, CommandResponse
from ..models.puzzle import get_puzzles


class HuntwordsPuzzlesCommand(object):
    """Command class that processes puzzles message"""

    def run(self, _request: CommandRequest) -> CommandResponse:
        """Command that processes puzzles message"""

        puzzles = get_puzzles()

        return CommandResponse(200, puzzles, {})
