
class PuzzleRepo:
    puzzles = dict[str, str]()
    puzzleboards = dict[str, list[str]]()

    def puzzle_by_name(self, name: str) -> str:
        '''accessor method to mock in unit test'''
        return self.puzzles.get(name, '')


_pr_instance: PuzzleRepo = PuzzleRepo()


def puzzle_repo() -> PuzzleRepo:
    return _pr_instance
