export class Point {
  x: number;
  y: number;
}

export class Puzzle {
  name: string;
  description: string;
  words: string[];
}

export class PuzzleBoard {
  height: number;
  width: number;
  letters: string[][];
  solutions: WordSolution[];
  puzzle: Puzzle;

  wordsToGo: number;
  completed: boolean;

  constructor(model?: PuzzleBoard) {
    if (model) {
      this.height = model.height;
      this.width = model.width;
      this.letters = model.letters;
      this.solutions = model.solutions;
      this.puzzle = model.puzzle;

      this.wordsToGo = model.wordsToGo || 0;
      this.completed = model.completed || false;
    } else {
      this.wordsToGo = 0;
      this.completed = false;
    }
  }
}

export class WordSolution {
  word: string;
  placed: boolean;
  origin: Point;
  direction: string;
  points: Point[];
  selected?: boolean;
}
