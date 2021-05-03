import json
from datetime import datetime

from .handler_models import Event, Response
from .model.puzzle import get_puzzle
from .model.puzzleboard import generate_puzzleboard, push_puzzleboard


class HuntwordsPuzzleBoardComsumedCommand(object):
    """Command class that processes puzzleboard-consumed message"""

    def run(self, event: Event, context) -> Response:
        """Command that processes puzzleboard-consumed message"""

        resp = json.loads(event.body)

        puzzle = get_puzzle(resp["puzzle"])
        size = int(resp["size"])

        pboard = generate_puzzleboard(size, size, puzzle=puzzle)

        push_puzzleboard(puzzle.name, pboard)

        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
        }

        return Response(200, json.dumps(resp), {})
