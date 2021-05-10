'''
Usage:
    manager puzzle_load (--file <filename>) [--url <url>]
    manager puzzle_del (--name <name>) [--url <url>]
    manager puzzles [--url <url>]
    manager puzzleboard_consume [--async-url <url>] (--name <name>) [--size <size>]
    manager puzzleboard_pop (--name <name>) [--url <url>]

Options:
    --async-url <url>    The url to the async function endpoint [default: http://localhost:8080/async-function/huntwordsapi]
    --url <url>          The url to the function [default: http://localhost:8080/function/huntwordsapi]

    --file <filename>    The filename from which to read the words; one per line
    --name <name>        The puzzle name to give the dictionary of words
    --size <size>        The length of a side of the grid on which to place words [default: 15]

    -h, --help           Print this help text and exit
    --version            Print the version and exit
'''
from docopt import docopt

from .commands_puzzleboard import command_puzzleboard_consume, command_puzzleboard_pop
from .commands_puzzle import command_puzzle_load, command_puzzles

# Command pattern
verbs = {
    'puzzle_load': command_puzzle_load,
    'puzzles': command_puzzles,
    'puzzleboard_consume': command_puzzleboard_consume,
    'puzzleboard_pop': command_puzzleboard_pop
}

if __name__ == '__main__':
    opts = docopt(__doc__, version='0.1')

    command = [v for k, v in verbs.items() if opts[k]][0]

    command(**opts)
