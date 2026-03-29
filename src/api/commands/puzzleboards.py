from datetime import datetime

from api.models.command import CommandRequest, CommandResponse
from api.models.puzzleboard import get_puzzleboards


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
