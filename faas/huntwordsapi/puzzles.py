import json

from .handler_models import Event, Response
from .model.puzzle import get_puzzles


class HuntwordsPuzzlesCommand(object):
    """Command class that processes puzzles message"""

    def run(self, event: Event, context) -> Response:
        """Command that processes puzzles message"""

        puzzles = get_puzzles()
        jpuzzles = json.dumps([dict(p) for p in puzzles])

        return Response(200, jpuzzles, {})
