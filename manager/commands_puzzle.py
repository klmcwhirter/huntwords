''' commands that work with redis '''


def command_puzzle_load(**kwargs):
    r = kwargs['redis']
    r.set('foo', 'bar')
    val = r.get('foo')
    print(f'foo={val}')
