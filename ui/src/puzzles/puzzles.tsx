import { createEffect, For } from 'solid-js';
import { useGame } from './game.context';
import { Puzzle } from './puzzle.model';
import { PuzzleSelectionView, PuzzleSelectEditView } from './puzzles.actions';

const PuzzlesView = (props) => {
  const game = useGame();

  const editPuzzle = (p: Puzzle) => game.editPuzzle(p);
  const selectPuzzle = (p: Puzzle) => game.selectPuzzle(p);

  createEffect(() => console.log('PuzzlesView: puzzleToEdit=', game.puzzleToEdit()));

  return (
    <div class='col-start-1 mt-0 h-[94vh] w-1/5 bg-emerald-200 p-2 align-top'>
      <h2 class='text-2xl font-semibold'>Puzzles</h2>
      <ul>
        <For each={game?.puzzles()}>
          {(p, i) => (
            <li class='p-2'>
              <PuzzleSelectionView puzzle={p} selectPuzzle={selectPuzzle} />
              <PuzzleSelectEditView puzzle={p} editPuzzle={editPuzzle} />
            </li>
          )}
        </For>
      </ul>
    </div>
  );
};

export default PuzzlesView;
