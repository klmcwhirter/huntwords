'''command adapter for huntwords api'''


from ..models.command import CommandResponse, request_from_dict
from .echo import HuntwordsEchoCommand
from .puzzle_updated import HuntwordsPuzzleUpdatedCommand
from .puzzleboard_consumed import HuntwordsPuzzleBoardConsumedCommand
from .puzzleboard_count import HuntwordsPuzzleBoardCountCommand
from .puzzleboard_pop import HuntwordsPuzzleBoardPopCommand
from .puzzleboards_clear import HuntwordsPuzzleBoardClearCommand
from .puzzles import HuntwordsPuzzlesCommand

commands = {
    'echo': HuntwordsEchoCommand,
    'puzzle-updated': HuntwordsPuzzleUpdatedCommand,
    'puzzles': HuntwordsPuzzlesCommand,
    'puzzleboards-clear': HuntwordsPuzzleBoardClearCommand,
    'puzzleboard-consumed': HuntwordsPuzzleBoardConsumedCommand,
    'puzzleboard-count': HuntwordsPuzzleBoardCountCommand,
    'puzzleboard-pop': HuntwordsPuzzleBoardPopCommand,
}


def handle_request(jreq: dict, **_kwargs):
    req = request_from_dict(jreq)

    if req.oper in commands:
        command = commands[req.oper]()
        rc = command.run(req)
        return dict(rc)

    return CommandResponse(404, f'{req.oper} is not recognized', {})
