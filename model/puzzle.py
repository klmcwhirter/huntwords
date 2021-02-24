''' models for the puzzle concept '''


def puzzle_urn(name):
    ''' redis universal resource name '''
    return f'urn:puzzle:{name}'


class Puzzle:
    def __init__(self, name, description, words):
        self.name = name
        self.description = description
        self.words = words

    def __iter__(self):
        ''' make class iterable so that transformation is easier via dict protocol '''
        yield 'name', self.name
        yield 'description', self.description
        yield 'words', self.words
