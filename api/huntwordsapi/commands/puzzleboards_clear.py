from datetime import datetime

from ..models.command import CommandRequest, CommandResponse
from ..models.puzzleboard import clear_puzzleboards


class HuntwordsPuzzleBoardClearCommand(object):
    """Command class that processes puzzleboards-clear message"""

    def run(self, request: CommandRequest) -> CommandResponse:
        """Command that processes puzzleboards-clear message"""

        resp = request.body

        clear_puzzleboards()

        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
        }

        return CommandResponse(200, resp, {})
