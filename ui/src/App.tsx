import type { Component } from 'solid-js';

import { GameStateProvider } from './puzzles/game.context';
import PuzzleBoardView from './puzzles/puzzleboard';
import PuzzlesView from './puzzles/puzzles';
import Toolbar from './toolbar';

const App: Component = () => {
  return (
    <GameStateProvider>
      <Toolbar />
      <div class='w-full'>
        <PuzzlesView />
        <PuzzleBoardView />
      </div>
    </GameStateProvider>
  );
};

export default App;
