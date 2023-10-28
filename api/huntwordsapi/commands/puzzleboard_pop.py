import logging
import sys
from datetime import datetime

import requests

from ..handler_models import Request, Response
from ..models.puzzleboard import pop_puzzleboard, PuzzleBoard


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

        rc = send_consumed(pboard)
        logging.info(rc)

        return Response(200, resp, {})


def send_consumed(pboard: PuzzleBoard):
    """Send async request to generate a new copy"""
    url = "http://gateway.openfaas:8080/async-function/huntwordsapi"

    data = f'{{ "oper": "puzzleboard-consumed", "body": {{ "puzzle": "{pboard.puzzle.name}", "size": {pboard.height} }} }}'

    return requests.post(url, data, {})
