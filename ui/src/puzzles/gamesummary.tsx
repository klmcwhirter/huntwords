import { Show } from 'solid-js';
import { useGame } from './game.context';

const GameSummary = (props) => {
  const game = useGame();

  return (
    <Show when={game.puzzleBoard()}>
      <div class='inline-block text-emerald-100'>
        <span class='ml-20 text-2xl font-bold text-blue-100'>
          {game.puzzleBoard().wordsNotSelectedCount}
        </span>
        <span class='text-lg text-blue-200'>
          {' / '}
          {game.puzzleBoard().wordsPlacedCount} words to go
        </span>

        <Show when={game.puzzleBoard().completed}>
          <span class='ml-20 text-2xl font-bold text-yellow-200'>
            Congratulations! You completed the puzzle.
          </span>
        </Show>
      </div>
    </Show>
  );
};

export default GameSummary;
