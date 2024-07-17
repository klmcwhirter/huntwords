import { For, Show } from 'solid-js';

import { useGame } from './game.context';

import BoardCellsView from './boardcells';
import BoardSummary from './boardsummary';

export const PuzzleBoardView = (props) => {
  const game = useGame();

  return (
    <Show when={game?.puzzleToEdit() === null}>
      <div class='mt-0 grid h-[94vh] grow grid-cols-3 gap-4 bg-blue-200 p-2 align-top'>
        <BoardCellsView />
        <BoardSummary />
      </div>
    </Show>
  );
};

export const PuzzleEditView = (props) => {
  const game = useGame();

  return (
    <Show when={game?.puzzleToEdit() !== null}>
      <div class='mt-0 grid h-[94vh] grow grid-cols-3 gap-4 bg-blue-200 p-2 align-top overflow-auto'>
        <For each={game.puzzleToEdit().words}>
          {(w, i) => (
            <div>{w}</div>
          )}
        </For>
      </div>
    </Show>
  );
};
