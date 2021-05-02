"""handler for huntwords api"""
from dataclasses import dataclass

from .puzzle_updated import HuntwordsPuzzleUpdatedCommand
from .puzzleboard_consumed import HuntwordsPuzzleBoardComsumedCommand
from .puzzleboard_pop import HuntwordsPuzzleBoardPopCommand


@dataclass
class Event:
    body: str
    headers: str
    method: str
    query: str
    path: str


@dataclass
class Response:
    statusCode: int
    body: str
    headers: dict


commands = {
    "puzzle-updated": HuntwordsPuzzleUpdatedCommand,
    "puzzleboard-consumed": HuntwordsPuzzleBoardComsumedCommand,
    "puzzleboard-pop": HuntwordsPuzzleBoardPopCommand,
}


def handle(event: Event, context):
    if event.path in commands:
        command = commands[event.path]()
        rc = command.run(event, context)
        return rc

    return Response(404, f"{event.path} is not recognized")
