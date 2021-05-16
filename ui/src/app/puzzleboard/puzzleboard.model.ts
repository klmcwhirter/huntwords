import { Puzzle } from '../puzzle/puzzle.model';

export class Point {
    x: number;
    y: number;

    constructor(
        x: number,
        y: number
    ) {
        this.x = x;
        this.y = y;
    }
}

export class PuzzleBoard {
    height: number;
    width: number;
    letters: string[][];
    solutions: WordSolution[];
    puzzle: Puzzle;

    constructor(
        height: number,
        width: number,
        letters: string[][],
        solutions: WordSolution[],
        puzzle: Puzzle
    ) {
        this.height = height;
        this.width = width;
        this.letters = letters;
        this.solutions = solutions.map(s => new WordSolution(s.word, s.placed, s.origin, s.direction, s.points));
        this.puzzle = new Puzzle(puzzle.name, puzzle.description, puzzle.words);
    }


    get displayedWordSolutions(): WordSolution[] {
        const rc = this.solutions.filter(s => s.placed);
        return rc;
    }

    // return the number of cols into which the place words will fit given the puzzle height
    get wordListCols(): number {
        const height = this.height || 1;
        const rc = Math.ceil(this.wordsPlacedCount / height);
        return rc;
    }

    // number of words placed
    get wordsPlacedCount(): number {
        const rc = this.solutions.filter(s => s.placed).length;
        return rc;
    }

    // number of words NOT selected
    get wordsNotSelectedCount(): number {
        const rc = this.wordsPlacedCount - this.wordsSelectedCount;
        return rc;
    }

    // number of selected words
    get wordsSelectedCount(): number {
        const rc = this.solutions.filter(s => s.selected).length;
        return rc;
    }
}

export const EMPTY_PUZZLEBOARD: PuzzleBoard = {
    height: 0,
    width: 0,
    letters: [] as string[][],
    solutions: [] as WordSolution[],
    puzzle: {
        name: '',
        description: '',
        words: [] as string[]
    },
    displayedWordSolutions: [] as WordSolution[],
    wordListCols: 0,
    wordsPlacedCount: 0,
    wordsNotSelectedCount: 0,
    wordsSelectedCount: 0
};

export class WordSolution {
    word: string;
    placed: boolean;
    origin: Point;
    direction: string;
    points: Point[];
    selected?: boolean;

    constructor(
        word: string,
        placed: boolean,
        origin: Point,
        direction: string,
        points: Point[]
    ) {
        this.word = word;
        this.placed = placed;
        this.origin = origin;
        this.direction = direction;
        this.points = points.map(p => new Point(p.x, p.y));
    }
}
