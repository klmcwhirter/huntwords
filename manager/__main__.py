'''
Usage:
    manager consume [--consume-url <url>] (--name <name>) [--size <size>]
    manager puzzle_get (--name <name>)
    manager puzzle_load (--file <filename>) [--load-url <url>]
    manager puzzle_del (--name <name>)

Options:
    --consume-url <url>  The url to the puzzleboard-consume function [default: http://localhost:8080/function/puzzleboard-consumed]
    --load-url <url>     The url to the puzzle-updated function [default: http://localhost:8080/function/puzzle-updated]

    --file <filename>    The filename from which to read the words; one per line
    --name <name>        The name to give the dictionary of words
    --size <size>        The length of a side of the grid on which to place words [default: 15]

    -h, --help           Print this help text and exit
    --version            Print the version and exit
'''
from docopt import docopt

from .commands_puzzleboard import command_puzzleboard_consume
from .commands_puzzle import command_puzzle_load

# Command pattern
verbs = {
    'consume': command_puzzleboard_consume,
    'puzzle_load': command_puzzle_load
}

if __name__ == '__main__':
    opts = docopt(__doc__, version='0.1')

    command = [v for k, v in verbs.items() if opts[k]][0]

    command(**opts)
