
from ..handler_models import Request, Response
from ..models.puzzle import get_puzzles


class HuntwordsPuzzlesCommand(object):
    """Command class that processes puzzles message"""

    def run(self, _request: Request) -> Response:
        """Command that processes puzzles message"""

        puzzles = get_puzzles()

        return Response(200, puzzles, {})
