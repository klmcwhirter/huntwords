from datetime import datetime

from ..models.command import CommandRequest, CommandResponse
from ..models.puzzleboard import get_puzzleboards


class HuntwordsPuzzleBoardsCommand(object):
    """Command class that processes puzzleboards message"""

    def run(self, request: CommandRequest) -> CommandResponse:
        """Command that processes puzzleboards message"""

        resp = request.body

        pboards = get_puzzleboards()

        resp = {
            "puzzleboards": dict(pboards),
            "processed": {
                "at": f"{datetime.now().isoformat()}",
            },
        }

        return CommandResponse(200, resp, {})
