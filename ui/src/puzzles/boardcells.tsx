import { For, Resource, Show } from 'solid-js';
import { useGame } from './game.context';
import { PuzzleBoard } from './puzzle.model';

const BoardCellsView = (props) => {
  const game = useGame();
  const board: Resource<PuzzleBoard> = game.puzzleBoard;

  return (
    <div class='col-span-2 inline-block'>
      <Show when={board.loading}>
        <p class='text-center text-5xl font-extrabold text-blue-700'>
          Loading {game.puzzleName()} ...
        </p>
      </Show>

      <Show when={board()}>
        <table>
          <For each={board().letters}>
            {(row, r) => (
              <tr>
                <For each={row}>
                  {(l, c) => (
                    <td
                      class='aspect-[2/1] w-16 p-2 text-center text-4xl font-semibold text-blue-700
                               hover:scale-110 hover:cursor-pointer hover:rounded-lg hover:bg-emerald-200'
                      classList={{
                        'bg-yellow-200 rounded-lg': board()?.isCellSelected(
                          r(),
                          c(),
                        ),
                      }}
                      onClick={() => {
                        const ws = board()?.toggleWordSelected(r(), c());
                        if (ws) {
                          game.selectWord(ws);
                        }
                      }}
                    >
                      {l}
                    </td>
                  )}
                </For>
              </tr>
            )}
          </For>
        </table>
      </Show>
    </div>
  );
};

export default BoardCellsView;
