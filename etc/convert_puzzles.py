'''convert original puzzle dump to current format'''

import sys

from json import dump, loads
from jmespath import search


def convert(filename, outfilename):
    jsonstr = ''
    with open(filename, 'r') as f:
        jsonstr = f.read()

    plist = loads(jsonstr)

    puzzles = search("[?puzzleWords].{name: name, description: description, words: puzzleWords[*].word}", plist)

    with open(outfilename, 'w') as outf:
        dump(puzzles, outf, indent=2)


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2])
