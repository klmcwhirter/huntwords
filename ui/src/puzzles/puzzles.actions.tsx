import { useGame } from './game.context';
import { Puzzle } from './puzzle.model';

export const PuzzleSelectionView = (props) => {
  const game = useGame();
  const p: Puzzle = props.puzzle;
  const selectPuzzle = props.selectPuzzle;

  return (
    <a
      class='p-2 text-md text-blue-700
    hover:rounded-lg hover:bg-emerald-500 hover:text-lg hover:font-semibold hover:text-white hover:cursor-pointer'
      classList={{
        'rounded-lg bg-emerald-500 text-lg font-semibold text-white':
          game.puzzleName() === p.name,
      }}
      onClick={(e) => selectPuzzle(p)}
    >
      {p.name} - {p.description}
    </a>
  );
};

export const PuzzleSelectEditView = (props) => {
  const game = useGame();
  const p: Puzzle = props.puzzle;
  const editPuzzle = props.editPuzzle;

  return (
    <a
      class='p-2 text-sm text-blue-700
    hover:rounded-lg hover:bg-emerald-100 hover:text-md hover:font-semibold hover:cursor-pointer'
    classList={{
      'rounded-lg bg-emerald-100 font-semibold text-md':
        game.puzzleToEdit()?.name === p.name,
    }}
    onClick={(e) => editPuzzle(p)}
    >
      &#9881;
    </a>
  );
};
