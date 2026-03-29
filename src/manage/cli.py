'''manager cli parser and AppContext model'''

import argparse
from dataclasses import dataclass, field
import os
from typing import Any

from manage.commands_puzzle import command_puzzle_load, command_puzzles

from manage.commands_puzzleboard import (
    command_puzzleboard_consume,
    command_puzzleboard_count,
    command_puzzleboard_pop,
    command_puzzleboards,
    command_puzzleboards_clear
)

# Command pattern
_verbs = {
    'puzzle_load': command_puzzle_load,
    'puzzles': command_puzzles,
    'puzzleboards': command_puzzleboards,
    'puzzleboards_clear': command_puzzleboards_clear,
    'puzzleboard_consume': command_puzzleboard_consume,
    'puzzleboard_count': command_puzzleboard_count,
    'puzzleboard_pop': command_puzzleboard_pop
}


@dataclass
class AppContext:
    opts: dict[str, Any] = field(default_factory=dict[str, Any])

    def command(self) -> None:
        from pprint import pprint
        pprint(self.opts, sort_dicts=False)

        command = _verbs[self.opts['verb']]

        command(**self.opts)

    @classmethod
    def verbs(cls) -> list[str]:
        return sorted(_verbs.keys())

    @staticmethod
    def from_namespace(ns: argparse.Namespace) -> AppContext:
        opts = vars(ns)
        return AppContext(opts=opts)


def parse_args(args: list[str], /, version: str = '1.0.0') -> AppContext:
    APP_HOST = os.environ.get('APP_HOST', 'api')
    APP_PORT = os.environ.get('APP_PORT', '3000')
    API_URL = os.environ.get('API_URL', f'http://{APP_HOST}:{APP_PORT}/api/')

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--version', action='store_true', help='show version and exit')

    verbs = parser.add_subparsers(title='verbs', required=False, dest='verb', metavar=f'({' | '.join(_verbs)})')

    puzzle_load_desc = 'load puzzle defs from file'
    puzzle_load_sub = verbs.add_parser('puzzle_load', description=puzzle_load_desc, help=puzzle_load_desc,
                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    puzzle_load_sub.add_argument('--file', required=True,
                                 help='The JSON filename from which to read the puzzle definitions')

    puzzles_desc = 'get loaded puzzle defs as JSON'
    puzzles_sub = verbs.add_parser('puzzles', description=puzzles_desc, help=puzzles_desc,
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    puzzlesboards_desc = 'get all generated puzzleboards as JSON'
    puzzlesboards_sub = verbs.add_parser('puzzleboards', description=puzzlesboards_desc, help=puzzlesboards_desc,
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    puzzlesboards_clear_desc = 'clear all generated puzzleboards from cache'
    puzzlesboards_clear_sub = verbs.add_parser('puzzleboards_clear',
                                               description=puzzlesboards_clear_desc, help=puzzlesboards_clear_desc,
                                               formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    pb_consume_desc = 'consume a puzzleboard for NAME, generate a new one and add it to cache'
    pb_consume_sub = verbs.add_parser('puzzleboard_consume',
                                      description=pb_consume_desc, help=pb_consume_desc,
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    pb_consume_sub.add_argument('--async-url', default=f'{API_URL}async/',
                                help='The base url to send async request')

    pb_count_desc = 'count the generated puzzleboards for NAME in the cache'
    pb_count_sub = verbs.add_parser('puzzleboard_count',
                                    description=pb_count_desc, help=pb_count_desc,
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    pb_pop_desc = 'pop a puzzleboard for NAME from the cache'
    pb_pop_sub = verbs.add_parser('puzzleboard_pop', description=pb_pop_desc, help=pb_pop_desc,
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    for p in [puzzle_load_sub, puzzles_sub, puzzlesboards_sub, puzzlesboards_clear_sub, pb_count_sub, pb_pop_sub]:
        p.add_argument('--url', default=API_URL, help='The base url to send request')

    for p in [pb_consume_sub, pb_count_sub, pb_pop_sub]:
        p.add_argument('--name', dest='name', required=True, help='The puzzle name on which to operate')

    pb_consume_sub.add_argument('--size', dest='size', type=int, default=15,
                                help='The length of a side of the grid on which to place words')

    pargs = parser.parse_args(args=args)

    if getattr(pargs, 'version', False):
        print(version)
        exit(0)

    return AppContext.from_namespace(ns=pargs)
