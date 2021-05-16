import { Component, OnInit } from '@angular/core';
import { Puzzle } from '../puzzle/puzzle.model';
import { PuzzlesService } from '../puzzleboard/puzzleboard.service';

@Component({
  selector: 'app-puzzle-select',
  templateUrl: './puzzle-select.component.html',
  styleUrls: ['./puzzle-select.component.scss']
})
export class PuzzleSelectComponent implements OnInit {

  puzzles: Puzzle[];
  puzzleName = '';

  constructor(private puzzlesSvc: PuzzlesService) {
    this.puzzles = [];

    this.puzzlesSvc.puzzles$.subscribe(puzzles => {
      this.puzzles = puzzles;
    });

    this.puzzlesSvc.getPuzzles();
  }

  ngOnInit(): void {
  }

  onPuzzleChange(puzzleName: string): void {
    console.log('onPuzzleChange:', puzzleName);
    this.puzzleName = puzzleName;
    this.puzzlesSvc.setPuzzleName(this.puzzleName);
  }
}
