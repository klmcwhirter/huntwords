import logging
import sys

from ..handler_models import Request, Response
from ..models.puzzleboard import count_puzzleboard


class HuntwordsPuzzleBoardCountCommand(object):
    """Command class that processes puzzleboard-count message"""

    def __init__(self):
        logging.basicConfig(stream=sys.stderr)

    def run(self, request: Request) -> Response:
        """Command that processes puzzleboard-count message"""

        req = request.body

        name = req["puzzle"]
        llen = count_puzzleboard(name)
        resp = {
            "puzzle": name,
            "count": llen
        }

        return Response(200, resp, {})
