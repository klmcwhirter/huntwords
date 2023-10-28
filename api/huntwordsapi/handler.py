'''handler for huntwords api'''
import json


from .handler_models import Response, request_from_dict
from .commands.echo import HuntwordsEchoCommand
from .commands.puzzle_updated import HuntwordsPuzzleUpdatedCommand
from .commands.puzzles import HuntwordsPuzzlesCommand
from .commands.puzzleboards_clear import HuntwordsPuzzleBoardClearCommand
from .commands.puzzleboard_consumed import HuntwordsPuzzleBoardComsumedCommand
from .commands.puzzleboard_pop import HuntwordsPuzzleBoardPopCommand

commands = {
    'echo': HuntwordsEchoCommand,
    'puzzle-updated': HuntwordsPuzzleUpdatedCommand,
    'puzzles': HuntwordsPuzzlesCommand,
    'puzzleboards-clear': HuntwordsPuzzleBoardClearCommand,
    'puzzleboard-consumed': HuntwordsPuzzleBoardComsumedCommand,
    'puzzleboard-pop': HuntwordsPuzzleBoardPopCommand,
}


def handle(jreq: dict):
    req = request_from_dict(jreq)

    if req.oper in commands:
        command = commands[req.oper]()
        rc = command.run(req)
        return dict(rc)

    return Response(404, f'{req.oper} is not recognized', {})
