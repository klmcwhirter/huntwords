export class Point {
  x: number;
  y: number;

  constructor(model?: Point) {
    if (model) {
      this.x = model.x;
      this.y = model.y;
    }
  }
}

export class Puzzle {
  name: string;
  description: string;
  words: string[];

  constructor(model?: Puzzle) {
    if (model) {
      this.name = model.name;
      this.description = model.description;
      this.words = [...model.words];
    }
  }

  static sort_array = (p1: Puzzle, p2: Puzzle) =>
    p1.name.localeCompare(p2.name);
}

export class WordSolution {
  word: string;
  placed: boolean;
  origin: Point;
  direction: string;
  points: Point[];
  selected?: boolean;

  constructor(model?: WordSolution) {
    if (model) {
      this.word = model.word;
      this.placed = model.placed;
      this.origin = new Point(model.origin);
      this.direction = model.direction;
      this.points = model.points.map((p) => new Point(p));
      this.selected = model.selected;
    }
  }

  containsCell(r: number, c: number): boolean {
    if (this.placed) {
      for (const cell of this.points) {
        if (cell.x === c && cell.y === r) {
          return true;
        }
      }
    }
    return false;
  }

  static sort_array = (s1: WordSolution, s2: WordSolution) =>
    s1.word.localeCompare(s2.word);
}

const initialCellSelected = (height: number, width: number): boolean[][] => {
  const rc = new Array(height);
  for (let i = 0; i < height; i++) {
    rc[i] = new Array(width);
    rc[i].fill(false);
  }
  return rc;
};

export class PuzzleBoard {
  height: number;
  width: number;
  letters: string[][];
  solutions: WordSolution[];
  puzzle: Puzzle;
  cellsSelected: boolean[][];

  constructor(model?: PuzzleBoard) {
    if (model) {
      this.height = model.height;
      this.width = model.width;
      this.letters = model.letters;
      this.solutions = model.solutions.map((ws) => new WordSolution(ws));
      this.puzzle = new Puzzle(model.puzzle);
      this.cellsSelected = model.cellsSelected
        ? JSON.parse(JSON.stringify(model.cellsSelected))
        : initialCellSelected(this.height, this.width);
    } else {
      this.cellsSelected = initialCellSelected(this.height, this.width);
    }
  }

  get completed(): boolean {
    return this.wordsNotSelectedCount <= 0;
  }

  get displayedWordSolutions(): WordSolution[] {
    const rc = this.solutions.filter((s) => s.placed);
    return rc;
  }

  isCellSelected(r: number, c: number): boolean {
    return this.cellsSelected[r][c];
  }

  setCellsForWordSelected(solution: WordSolution, value: boolean): void {
    for (const cell of solution.points) {
      // This cell may be an intersection point for multiple solutions
      const selectedCells = this.findSolutions(cell.y, cell.x).filter(
        (s) => s.selected,
      );

      if (selectedCells.length >= 1) {
        this.cellsSelected[cell.y][cell.x] = true;
      } else {
        // If this cell intersects another solution don't change it!
        this.cellsSelected[cell.y][cell.x] = value;
      }
    }
  }

  toggleWordSelected = (r: number, c: number): WordSolution => {
    console.log(`toggleWordSelected: r=${r}, c=${c}`);
    const solutions = this.findSolutions(r, c);
    let rc: WordSolution = null;

    if (solutions.length === 1) {
      rc = solutions[0];
      const wasSelected = rc.selected;

      rc.selected = !wasSelected;
      this.setCellsForWordSelected(rc, !wasSelected);

      const verb = wasSelected ? 'unselected' : 'found';
      console.log(`You ${verb} ${rc.word}`);
    }

    return rc;
  };

  // return the number of cols into which the place words will fit given the puzzle height
  get wordListCols(): number {
    const height = this.height || 1;
    const rc = Math.ceil(this.wordsPlacedCount / height);
    return rc;
  }

  // number of words placed
  get wordsPlacedCount(): number {
    const rc = this.solutions.filter((s) => s.placed).length;
    return rc;
  }

  // number of words NOT selected
  get wordsNotSelectedCount(): number {
    const rc = this.wordsPlacedCount - this.wordsSelectedCount;
    return rc;
  }

  // number of selected words
  get wordsSelectedCount(): number {
    const rc = this.solutions.filter((s) => s.selected).length;
    return rc;
  }

  findSolutions(r: number, c: number): WordSolution[] {
    const solutions = this.solutions.filter((ws: WordSolution) =>
      ws.containsCell(r, c),
    );
    return solutions;
  }
}
