import { type Component } from 'solid-js';

import { GameStateProvider } from './puzzles/game.context';
import { PuzzleBoardView, PuzzleEditView } from './puzzles/puzzleboard';
import PuzzlesView from './puzzles/puzzles';
import Toolbar from './toolbar';

const App: Component = () => {

  return (
    <GameStateProvider>
      <Toolbar />
      <div class='flex w-full gap-0'>
        <PuzzlesView />
        <PuzzleBoardView />
        <PuzzleEditView />
      </div>
    </GameStateProvider>
  );
};

export default App;
