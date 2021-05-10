'''handler for huntwords api'''
import json

from .handler_models import Event, Response, request_from_dict
from .puzzle_updated import HuntwordsPuzzleUpdatedCommand
from .puzzles import HuntwordsPuzzlesCommand
from .puzzleboard_consumed import HuntwordsPuzzleBoardComsumedCommand
from .puzzleboard_pop import HuntwordsPuzzleBoardPopCommand

commands = {
    'puzzle-updated': HuntwordsPuzzleUpdatedCommand,
    'puzzles': HuntwordsPuzzlesCommand,
    'puzzleboard-consumed': HuntwordsPuzzleBoardComsumedCommand,
    'puzzleboard-pop': HuntwordsPuzzleBoardPopCommand,
}


def handle(event: Event, context):
    jreq = json.loads(event.body)
    req = request_from_dict(jreq)

    if req.oper in commands:
        command = commands[req.oper]()
        event.request = req
        rc = command.run(event, context)
        return dict(rc)  # send dict back to index.py

    return Response(404, f'{req.oper} is not recognized', {})
