import { Component } from '@angular/core';
import { GameStateService } from './game-state.service';

@Component({
  selector: 'app-game-state',
  templateUrl: './game-state.component.html',
  styleUrls: ['./game-state.component.scss']
})
export class GameStateComponent {

  constructor(public gameStateSvc: GameStateService) { }

}
