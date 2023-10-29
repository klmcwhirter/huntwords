import { For } from 'solid-js';
import { useGame } from './game.context';
import { Puzzle } from './puzzle.model';

const PuzzlesView = (props) => {
  const game = useGame();

  const completeGame = (e) => game.complete();
  const selectPuzzle = (p: Puzzle) => game.selectPuzzle(p);

  return (
    <div class='mt-0 inline-block h-fit w-1/5 bg-emerald-200 p-2 align-top'>
      <h2>Puzzles</h2>
      <ul>
        <For each={game.puzzles()}>
          {(p, i) => (
            <li class='p-2'>
              <span
                class='p-2 text-blue-800 hover:cursor-pointer hover:rounded-lg hover:bg-emerald-500
                hover:text-blue-100 hover:underline'
                onClick={(e) => selectPuzzle(p)}
              >
                {p.name} - {p.description}
              </span>
            </li>
          )}
        </For>
      </ul>
      <button onClick={completeGame}>Complete</button>
    </div>
  );
};

export default PuzzlesView;
