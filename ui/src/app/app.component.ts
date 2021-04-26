import { Component } from '@angular/core';
import { Puzzle } from './puzzle/puzzle.model';
import { PuzzleBoard } from './puzzleboard/puzzleboard.model';
import { PuzzleBoardService } from './puzzleboard/puzzleboard.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  pb = '';

  constructor(pbSvc: PuzzleBoardService) {
    pbSvc.getPuzzleBoard('').subscribe(pb => this.pb = JSON.stringify(pb));
  }
}
