
import { Component, Input, OnInit } from '@angular/core';
import { Location } from '@angular/common';
// import { ActivatedRoute } from '@angular/router';

import {
  EMPTY_PUZZLEBOARD,
  PuzzleBoard,
  WordSolution,
} from './puzzleboard.model';
import { PuzzleBoardService } from './puzzleboard.service';

// import { PuzzleDoneService } from '../puzzle-done/puzzle-done.service';

// import { SnackService } from '../utils/snack.service';
// import { WindowReloadService } from '../utils/window-reload.service';

@Component({
  templateUrl: './puzzleboard.component.html',
  styleUrls: ['./puzzleboard.component.scss'],
  providers: [],
})
export class PuzzleComponent implements OnInit {
  // The puzzle
  @Input() puzzleBoard: PuzzleBoard = EMPTY_PUZZLEBOARD;
  // The cells containing the word the user has requested a hint
  hint: boolean[][] = [];
  // The number of hints the user has requested
  numHints = 0;
  // The cells that are selected
  selected: boolean[][] = [];

  constructor(
    // private activatedRoute: ActivatedRoute,
    private location: Location,
    private pbSvc: PuzzleBoardService,
    // private puzzleDoneService: PuzzleDoneService,
    // private snackService: SnackService,
    // private windowReloadService: WindowReloadService
  ) { }

  ngOnInit() {
    // const puzzleBoard = <IPuzzleBoard>this.activatedRoute.snapshot.data['board'];
    this.pbSvc.getPuzzleBoard('').subscribe(pb => this.puzzleBoard = new PuzzleBoard(pb.height, pb.width, pb.letters, pb.solutions, pb.puzzle));
    this.clearCellsHints();
    this.clearCellsSelected();
  }

  /* ------------------------- */
  /* METHODS THAT USE SERVICES */
  /* ------------------------- */

  // Use puzzleDoneService to display PuzzleDoneComponent - if puzzle has been completed
  maybeCompletePuzzle(): void {
    // if (this.puzzleBoard.wordsNotSelectedCount <= 0) {
    //     this.puzzleDoneService.completePuzzle(this.puzzleBoard)
    //         .subscribe(playAgain => {
    //             if (playAgain) {
    //                 this.windowReloadService.reload();
    //             }
    //         });
    // }
  }

  /* ------------------------------------- */
  /* METHODS THAT OPERATE ON HELPER ARRAYS */
  /* ------------------------------------- */

  clearArray(array: boolean[][]): boolean[][] {
    array = [];
    for (let r = 0; r < this.puzzleBoard.height; r++) {
      array[r] = [];
      for (let c = 0; c < this.puzzleBoard.width; c++) {
        array[r][c] = false;
      }
    }
    return array;
  }

  clearCellsHints() {
    this.hint = this.clearArray(this.hint);
  }

  clearCellsSelected(): void {
    this.selected = this.clearArray(this.selected);
  }

  setCellsForWordHint(solution: WordSolution, value: boolean): void {
    for (const cell of solution.points) {
      this.hint[cell.y][cell.x] = value;
    }
  }

  /* ----------------------------- */
  /* METHODS THAT PROVIDE BEHAVIOR */
  /* ----------------------------- */

  back(): void {
    this.location.back();
  }

  // This uses async / await so that we are sure the cells have been reset
  // before allowing the view to re-render
  async showSnackAndReset(solution: WordSolution): Promise<void> {
    // const msg = `${solution.word} : ${solution.direction} @ ${originToString(solution.origin)}`;
    // const promise = this.snackService.open(msg, { duration: 1000 })
    //     .afterDismissed()
    //     .toPromise();

    // await promise.then(() => {
    //     this.clearCellsHints();
    //     if (solution.selected) {
    //         this.setCellsForWordSelected(solution, true);
    //     }
    // });
  }

  showHint(solution: WordSolution): void {
    // if (this.numHints >= this.puzzleBoard.displayedWordSolutions.length / 3) {
    //     this.snackService.open('Number of hints exceeded');
    //     return;
    // }

    // if (solution.selected) {
    //     this.setCellsForWordSelected(solution, false);
    // } else {
    //     this.numHints++;
    // }

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
      // const selected = this.findSolutions(cell.y, cell.x).filter(s => s.selected);

      // If this cell intersects another solution don't change it!
      // if (selected.length <= 1) {
      //     this.selected[cell.y][cell.x] = value;
      // }
    }
  }

  toggleWordSelected(r: number, c: number): void {
    const solutions = this.findSolutions(r, c);

    if (solutions.length === 1) {
      const solution = solutions[0];
      // const wasSelected = solution.selected;


      // this.setCellsForWordSelected(solution, !wasSelected);
      // solution.selected = !wasSelected;

      // const verb = (wasSelected) ? 'unselected' : 'found';
      // this.snackService.open(`You ${verb} ${solution.word}`, { duration: 1000 });

      this.maybeCompletePuzzle();
    }
  }
}
