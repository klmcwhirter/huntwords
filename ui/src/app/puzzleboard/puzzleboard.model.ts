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
}

export const EMPTY_PUZZLEBOARD: PuzzleBoard = {
    height: 0,
    width: 0,
    letters: [],
    solutions: [],
    puzzle: {
        name: '',
        description: '',
        words: []
    }
};

export class WordSolution {
    word: string;
    placed: boolean;
    origin: Point;
    direction: string;
    points: Point[];

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
