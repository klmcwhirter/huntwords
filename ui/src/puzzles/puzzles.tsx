import { For } from 'solid-js';
import { useGame } from './game.context';
import { Puzzle } from './puzzle.model';

const PuzzlesView = (props) => {
  const game = useGame();

  const selectPuzzle = (p: Puzzle) => game.selectPuzzle(p);

  return (
    <div class='col-start-1 mt-0 h-[94vh] w-1/5 bg-emerald-200 p-2 align-top'>
      <h2 class='text-2xl font-semibold'>Puzzles</h2>
      <ul>
        <For each={game?.puzzles()}>
          {(p, i) => (
            <li class='p-2'>
              <a
                class='p-2 text-lg text-blue-700
                hover:rounded-lg hover:bg-emerald-500 hover:font-semibold hover:text-white hover:cursor-pointer'
                classList={{
                  'rounded-lg bg-emerald-500 font-semibold text-white':
                    game.puzzleName() === p.name,
                }}
                onClick={(e) => selectPuzzle(p)}
              >
                {p.name} - {p.description}
              </a>
            </li>
          )}
        </For>
      </ul>
    </div>
  );
};

export default PuzzlesView;
