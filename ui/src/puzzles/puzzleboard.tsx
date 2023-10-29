import { Show } from 'solid-js';
import { Game, useGame } from './game.context';

const PuzzleBoardView = (props) => {
  const game: Game = useGame();

  return (
    <div class='mt-0 inline-block h-fit w-4/5 bg-blue-200 p-2 align-top '>
      PuzzleBoard
      <Show when={game.puzzleBoard()}>
        <span class='p-2'>{game.puzzleBoard().puzzle.name}</span>
      </Show>
    </div>
  );
};

export default PuzzleBoardView;
