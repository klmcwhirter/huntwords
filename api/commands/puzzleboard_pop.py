import logging
import sys
from datetime import datetime

from ..models.command import CommandRequest, CommandResponse
from ..models.puzzleboard import pop_puzzleboard


class HuntwordsPuzzleBoardPopCommand(object):
    """Command class that processes puzzleboard-pop message"""

    def __init__(self):
        logging.basicConfig(stream=sys.stderr)

    def run(self, request: CommandRequest) -> CommandResponse:
        """Command that processes puzzleboard-pop message"""

        req = request.body

        pboard = pop_puzzleboard(req["puzzle"])

        resp = {
            "puzzleboard": dict(pboard),
            "processed": {
                "at": f"{datetime.now().isoformat()}",
            },
        }

        return CommandResponse(200, resp, {})
