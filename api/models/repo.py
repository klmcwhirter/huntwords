
class PuzzleRepo:
    puzzles = dict[str, str]()
    puzzleboards = dict[str, list[str]]()

    def puzzle_by_name(self, name: str) -> str:
        '''accessor method to mock in unit test'''
        return self.puzzles.get(name, '')

    def count_puzzleboard(self, name: str) -> int:
        '''Count puzzleboard lists'''
        llen = len(self.puzzleboards.get(name, []))
        return llen


_pr_instance: PuzzleRepo = PuzzleRepo()


def puzzle_repo() -> PuzzleRepo:
    return _pr_instance
