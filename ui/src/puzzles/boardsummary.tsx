import { For, Resource, Show } from 'solid-js';
import { PuzzleBoard, WordSolution } from './puzzle.model';
import { Game, useGame } from './game.context';

const BoardSummary = (props) => {
  const game = useGame();
  const board: Resource<PuzzleBoard> = game.puzzleBoard;

  return (
    <Show when={board()}>
      <div class='grid h-fit grid-cols-2 gap-1'>
        <For each={board().solutions.toSorted(WordSolution.sort_array)}>
          {(ws) => (
            <p
              class='p-2 text-lg font-semibold text-blue-800
                   hover:cursor-pointer hover:rounded-lg hover:bg-emerald-200 hover:text-center'
              classList={{ 'line-through text-slate-400': ws.selected }}
              onClick={() => game.hintRequested(ws)}
            >
              {ws.word}
            </p>
          )}
        </For>

        <p class='col-span-2 p-4 text-lg text-blue-600'>
          {Game.MAX_HINTS - game.hints().length} of {Game.MAX_HINTS} hints
          remaining
        </p>
      </div>
    </Show>
  );
};

export default BoardSummary;
