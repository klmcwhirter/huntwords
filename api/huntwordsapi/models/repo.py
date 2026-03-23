
class PuzzleRepo:
    puzzles = dict[str, str]()
    puzzleboards = dict[str, list[str]]()


_pr_instance: PuzzleRepo = PuzzleRepo()


def puzzle_repo() -> PuzzleRepo:
    return _pr_instance
