// An app-wide service implementation

import {
  Resource,
  createContext,
  createResource,
  createSignal,
  useContext,
} from 'solid-js';
import { Puzzle, PuzzleBoard } from './puzzle.model';
import { fetchPuzzleBoard, fetchPuzzles } from './puzzles.service';

export class Game {
  constructor(
    public puzzles: Resource<Puzzle[]>,
    public puzzleBoard: Resource<PuzzleBoard>,
    public complete: () => void,
    public selectPuzzle: (p: Puzzle) => void,
  ) {}
}

const GameStateContext = createContext<Game>();

export const GameStateProvider = (props) => {
  const [puzzles] = createResource(fetchPuzzles);
  const [puzzleName, setPuzzleName] = createSignal(null);
  const [puzzleBoard, { mutate: mutatePuzzleBoard }] = createResource(
    puzzleName,
    fetchPuzzleBoard,
    {
      initialValue: null,
    },
  );

  const game = new Game(
    puzzles,
    puzzleBoard,
    // complete
    () =>
      mutatePuzzleBoard((pb) => {
        const new_pb = new PuzzleBoard({ ...pb, completed: true });
        return new_pb;
      }),
    // selectGame
    (p: Puzzle) => setPuzzleName((g) => p.name),
  );

  return (
    <GameStateContext.Provider value={game}>
      {props.children}
    </GameStateContext.Provider>
  );
};

export const useGame = () => useContext<Game>(GameStateContext);
