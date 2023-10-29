from datetime import datetime

from ..handler_models import Request, Response
from ..models.puzzle import get_puzzle
from ..models.puzzleboard import generate_puzzleboard, push_puzzleboard


class HuntwordsPuzzleBoardConsumedCommand(object):
    """Command class that processes puzzleboard-consumed message"""

    def run(self, request: Request) -> Response:
        """Command that processes puzzleboard-consumed message"""

        resp = request.body

        puzzle = get_puzzle(resp["puzzle"])
        size = int(resp["size"])

        pboard = generate_puzzleboard(size, size, puzzle=puzzle)

        push_puzzleboard(puzzle.name, pboard)

        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
        }

        return Response(200, resp, {})
