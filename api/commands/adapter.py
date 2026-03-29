'''command adapter for huntwords api'''


from api.models.command import CommandResponse, request_from_dict

from api.commands.echo import HuntwordsEchoCommand
from api.commands.puzzle_updated import HuntwordsPuzzleUpdatedCommand
from api.commands.puzzleboard_consumed import HuntwordsPuzzleBoardConsumedCommand
from api.commands.puzzleboard_count import HuntwordsPuzzleBoardCountCommand
from api.commands.puzzleboard_pop import HuntwordsPuzzleBoardPopCommand
from api.commands.puzzleboards import HuntwordsPuzzleBoardsCommand
from api.commands.puzzleboards_clear import HuntwordsPuzzleBoardClearCommand
from api.commands.puzzles import HuntwordsPuzzlesCommand

commands = {
    'echo': HuntwordsEchoCommand,
    'puzzle-updated': HuntwordsPuzzleUpdatedCommand,
    'puzzles': HuntwordsPuzzlesCommand,
    'puzzleboards': HuntwordsPuzzleBoardsCommand,
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
