
import { Component } from '@angular/core';

import {
  EMPTY_PUZZLEBOARD,
  PuzzleBoard,
  WordSolution,
} from './puzzleboard.model';
import { PuzzlesService } from './puzzleboard.service';
import { GameStateService } from '../game-state/game-state.service';

@Component({
  selector: 'app-puzzleboard',
  templateUrl: './puzzleboard.component.html',
  styleUrls: ['./puzzleboard.component.scss'],
  providers: [],
})
export class PuzzleBoardComponent {
  // The puzzle
  puzzleBoard: PuzzleBoard = EMPTY_PUZZLEBOARD;
  // The cells containing the word the user has requested a hint
  hint: boolean[][] = [];
  // The number of hints the user has requested
  numHints = 0;
  // The cells that are selected
  selected: boolean[][] = [];

  constructor(
    private gameStateSvc: GameStateService,
    private puzzlesSvc: PuzzlesService,
  ) {
    this.puzzlesSvc.puzzlesBoard$.subscribe(pb => {
      this.puzzleBoard = pb;
      this.gameStateSvc.reset(pb.puzzle.name, pb.puzzle.description, pb.wordsNotSelectedCount);
      this.clearCellsHints();
      this.clearCellsSelected();
    });
  }

  /* ------------------------- */
  /* METHODS THAT USE SERVICES */
  /* ------------------------- */

  maybeCompletePuzzle(): void {
    this.gameStateSvc.state.wordsToGo = this.puzzleBoard.wordsNotSelectedCount;

    if (this.puzzleBoard.wordsNotSelectedCount <= 0) {
      console.log('Game complete.');
      this.gameStateSvc.state.complete = true;
    }
  }

  /* ------------------------------------- */
  /* METHODS THAT OPERATE ON HELPER ARRAYS */
  /* ------------------------------------- */

  clearArray(): boolean[][] {
    const array: boolean[][] = [];
    for (let r = 0; r < this.puzzleBoard.height; r++) {
      array[r] = [];
      for (let c = 0; c < this.puzzleBoard.width; c++) {
        array[r][c] = false;
      }
    }
    return array;
  }

  clearCellsHints(): void {
    this.hint = this.clearArray();
  }

  clearCellsSelected(): void {
    this.selected = this.clearArray();
  }

  setCellsForWordHint(solution: WordSolution, value: boolean): void {
    for (const cell of solution.points) {
      this.hint[cell.y][cell.x] = value;
    }
  }

  /* ----------------------------- */
  /* METHODS THAT PROVIDE BEHAVIOR */
  /* ----------------------------- */

  // This uses async / await so that we are sure the cells have been reset
  // before allowing the view to re-render
  async showSnackAndReset(solution: WordSolution): Promise<void> {
    await setTimeout(() => {
      this.clearCellsHints();
      if (solution.selected) {
        this.setCellsForWordSelected(solution, true);
      }
    }, 1000);
  }

  showHint(solution: WordSolution): void {
    if (this.numHints >= this.puzzleBoard.displayedWordSolutions.length / 3) {
      console.log('Number of hints exceeded');
      return;
    }

    if (solution.selected) {
      this.setCellsForWordSelected(solution, false);
    } else {
      this.numHints++;
    }

    this.setCellsForWordHint(solution, true);

    this.showSnackAndReset(solution);
  }

  findSolutions(r: number, c: number): WordSolution[] {
    const solutions = this.puzzleBoard.solutions.filter(this.solutionContainsCell(r, c));
    return solutions;
  }

  solutionContainsCell(r: number, c: number): (s: WordSolution) => boolean {
    return function (solution: WordSolution): boolean {
      if (solution.placed) {
        for (const cell of solution.points) {
          if (cell.x === c && cell.y === r) {
            return true;
          }
        }
      }
      return false;
    };
  }

  setCellsForWordSelected(solution: WordSolution, value: boolean): void {
    for (const cell of solution.points) {
      // This cell may be an intersection point for multiple solutions
      const selected = this.findSolutions(cell.y, cell.x).filter(s => s.selected);

      // If this cell intersects another solution don't change it!
      if (selected.length <= 1) {
        this.selected[cell.y][cell.x] = value;
      }
    }
  }

  toggleWordSelected(r: number, c: number): void {
    const solutions = this.findSolutions(r, c);

    if (solutions.length === 1) {
      const solution = solutions[0];
      const wasSelected = solution.selected;


      this.setCellsForWordSelected(solution, !wasSelected);
      solution.selected = !wasSelected;

      const verb = (wasSelected) ? 'unselected' : 'found';
      console.log(`You ${verb} ${solution.word}`);

      this.maybeCompletePuzzle();
    }
  }
}
