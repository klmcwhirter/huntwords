import logging
import sys
from datetime import datetime

import requests

from ..handler_models import Request, Response
from ..models.puzzleboard import pop_puzzleboard


class HuntwordsPuzzleBoardPopCommand(object):
    """Command class that processes puzzleboard-pop message"""

    def __init__(self):
        logging.basicConfig(stream=sys.stderr)

    def run(self, request: Request) -> Response:
        """Command that processes puzzleboard-pop message"""

        req = request.body

        pboard = pop_puzzleboard(req["puzzle"])

        resp = {
            "puzzleboard": dict(pboard),
            "processed": {
                "at": f"{datetime.now().isoformat()}",
            },
        }

        return Response(200, resp, {})
