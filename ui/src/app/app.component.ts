import { Component } from '@angular/core';
import { EMPTY_PUZZLEBOARD, PuzzleBoard } from './puzzleboard/puzzleboard.model';
import { PuzzleBoardService } from './puzzleboard/puzzleboard.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  pb = EMPTY_PUZZLEBOARD;

  constructor(pbSvc: PuzzleBoardService) {
    pbSvc.getPuzzleBoard('').subscribe(pb => this.pb = pb);
  }
}
