import json
from datetime import datetime

from .handler_models import Event, Response
from .model.puzzleboard import clear_puzzleboards


class HuntwordsPuzzleBoardClearCommand(object):
    """Command class that processes puzzleboards-clear message"""

    def run(self, event: Event, context) -> Response:
        """Command that processes puzzleboards-clear message"""

        resp = event.request.body

        clear_puzzleboards()

        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
        }

        return Response(200, json.dumps(resp), {})
