import { Injectable } from '@angular/core';

export class GameState {
  puzzleName: string;
  puzzleDesc: string;
  wordsToGo: number;
  complete: boolean;

  constructor(
    puzzleName: string = '',
    puzzleDesc: string = '',
    wordsToGo: number = 0,
    complete: boolean = false
  ) {
    this.puzzleName = puzzleName;
    this.puzzleDesc = puzzleDesc;
    this.wordsToGo = wordsToGo;
    this.complete = complete;
  }
}

@Injectable({
  providedIn: 'root'
})
export class GameStateService {
  state: GameState = new GameState();

  constructor() { }

  reset(name: string, desc: string, wordsToGo: number): void {
    this.state = new GameState(name, desc, wordsToGo);
  }
}
