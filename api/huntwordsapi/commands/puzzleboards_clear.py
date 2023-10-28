from datetime import datetime

from ..handler_models import Request, Response
from ..models.puzzleboard import clear_puzzleboards


class HuntwordsPuzzleBoardClearCommand(object):
    """Command class that processes puzzleboards-clear message"""

    def run(self, request: Request) -> Response:
        """Command that processes puzzleboards-clear message"""

        resp = request.body

        clear_puzzleboards()

        resp["processed"] = {
            "at": f"{datetime.now().isoformat()}",
        }

        return Response(200, resp, {})
