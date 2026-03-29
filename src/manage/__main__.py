'''manage entrypoint'''

import sys

from manage.cli import parse_args

if __name__ == '__main__':
    ctx = parse_args(sys.argv[1:])

    ctx.command()
