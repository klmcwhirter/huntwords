import { Show } from 'solid-js';
import { useGame } from './game.context';

const GameSummary = (props) => {
  const game = useGame();

  return (
    <Show when={game.puzzleBoard()?.puzzle?.name}>
      <div class='ml-20 inline-block text-green-100'>
        <span class='text-lg'>{game.puzzleBoard().puzzle.name}</span>

        <Show when={game.puzzleBoard().puzzle.description}>
          <span class='text-base'>
            {' '}
            - {game.puzzleBoard().puzzle.description}
          </span>
        </Show>

        <span class='ml-20 text-lg text-blue-200'>
          {game.puzzleBoard().wordsToGo} words to go
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
