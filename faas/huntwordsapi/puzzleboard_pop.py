import json
import logging
import sys
from datetime import datetime

import requests

from .handler_models import Event, Response
from .model.puzzleboard import pop_puzzleboard


class HuntwordsPuzzleBoardPopCommand(object):
    """Command class that processes puzzleboard-pop message"""

    def __init__(self):
        logging.basicConfig(stream=sys.stderr)

    def run(self, event: Event, context):
        """Command that processes puzzleboard-pop message"""

        req = json.loads(event.body)

        pboard = pop_puzzleboard(req["puzzle"])
        jpboard = json.dumps(dict(pboard))

        resp = {
            "puzzleboard": jpboard,
            "processed": {
                "at": f"{datetime.now().isoformat()}",
            },
        }

        rc = send_consumed(pboard)
        logging.info(rc)

        return Response(200, json.dumps(resp))


def send_consumed(pboard):
    """Send async request to generate a new copy"""
    url = "http://puzzleboard-consumed.openfaas-fn:8080"

    data = f'{{"puzzle": "{pboard.puzzle.name}" }}'

    return requests.post(url, data, {})
