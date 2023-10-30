'''handler for huntwords api'''
import json

from .commands.echo import HuntwordsEchoCommand
from .commands.puzzle_updated import HuntwordsPuzzleUpdatedCommand
from .commands.puzzleboard_consumed import HuntwordsPuzzleBoardConsumedCommand
from .commands.puzzleboard_count import HuntwordsPuzzleBoardCountCommand
from .commands.puzzleboard_pop import HuntwordsPuzzleBoardPopCommand
from .commands.puzzleboards_clear import HuntwordsPuzzleBoardClearCommand
from .commands.puzzles import HuntwordsPuzzlesCommand
from .handler_models import Response, request_from_dict

commands = {
    'echo': HuntwordsEchoCommand,
    'puzzle-updated': HuntwordsPuzzleUpdatedCommand,
    'puzzles': HuntwordsPuzzlesCommand,
    'puzzleboards-clear': HuntwordsPuzzleBoardClearCommand,
    'puzzleboard-consumed': HuntwordsPuzzleBoardConsumedCommand,
    'puzzleboard-count': HuntwordsPuzzleBoardCountCommand,
    'puzzleboard-pop': HuntwordsPuzzleBoardPopCommand,
}


def handle(jreq: dict):
    req = request_from_dict(jreq)

    if req.oper in commands:
        command = commands[req.oper]()
        rc = command.run(req)
        return dict(rc)

    return Response(404, f'{req.oper} is not recognized', {})
