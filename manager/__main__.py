'''
Usage:
    manager puzzle_load (--file <filename>) [--url <url>]
    manager puzzles [--url <url>]
    manager puzzleboards_clear [--url <url>]
    manager puzzleboard_consume [--url <url>] (--name <name>) [--size <size>]
    manager puzzleboard_count [--url <url>] (--name <name>)
    manager puzzleboard_pop (--name <name>) [--url <url>]

Options:
    --url <url>          The url to the function [default: http://localhost:8090/api/]

    --file <filename>    The filename from which to read the words; one per line
    --name <name>        The puzzle name on which to operate
    --size <size>        The length of a side of the grid on which to place words [default: 15]

    -h, --help           Print this help text and exit
    --version            Print the version and exit
'''
from docopt import docopt

from .commands_puzzle import command_puzzle_load, command_puzzles
from .commands_puzzleboard import (command_puzzleboard_consume,
                                   command_puzzleboard_count,
                                   command_puzzleboard_pop,
                                   command_puzzleboards_clear)

# Command pattern
verbs = {
    'puzzle_load': command_puzzle_load,
    'puzzles': command_puzzles,
    'puzzleboards_clear': command_puzzleboards_clear,
    'puzzleboard_consume': command_puzzleboard_consume,
    'puzzleboard_count': command_puzzleboard_count,
    'puzzleboard_pop': command_puzzleboard_pop
}

if __name__ == '__main__':
    opts = docopt(__doc__, version='0.1')

    command = [v for k, v in verbs.items() if opts[k]][0]

    command(**opts)
