// An app-wide service implementation

import {
  Accessor,
  Resource,
  createContext,
  createResource,
  createSignal,
  useContext,
} from 'solid-js';
import { Puzzle, PuzzleBoard, WordSolution } from './puzzle.model';
import { fetchPuzzleBoard, fetchPuzzles } from './puzzles.service';

export class Game {
  static MAX_HINTS = 5;
  constructor(
    public puzzles: Resource<Puzzle[]>,
    public puzzleBoard: Resource<PuzzleBoard>,
    public puzzleName: Accessor<string>,
    public hints: Accessor<string[]>,

    public hintRequested: (ws: WordSolution) => void,
    public selectPuzzle: (p: Puzzle) => void,
    public selectWord: (ws: WordSolution) => void,
  ) {}
}

const GameStateContext = createContext<Game>();

export const GameStateProvider = (props) => {
  const [hints, setHints] = createSignal<string[]>([]);
  const [puzzles] = createResource(fetchPuzzles);
  const [puzzleName, setPuzzleName] = createSignal<string>(null);
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
    puzzleName,
    hints,
    // hintRequested
    (ws: WordSolution) => {
      if (
        !ws.selected &&
        (hints().includes(ws.word) || hints().length < Game.MAX_HINTS)
      ) {
        puzzleBoard().setCellsForWordSelected(ws, true);
        mutatePuzzleBoard((pb) => new PuzzleBoard(pb));
        setTimeout(() => {
          puzzleBoard().setCellsForWordSelected(ws, false);
          mutatePuzzleBoard((pb) => new PuzzleBoard(pb));
        }, 2000);
        if (!hints().includes(ws.word)) {
          setHints((h) => [...h, ws.word]);
        }
      }
    },
    // selectGame
    (p: Puzzle) => {
      setPuzzleName(null);
      mutatePuzzleBoard(null);
      setPuzzleName((g) => p.name);
      setHints((h) => []);
    },
    // selectWord
    (ws: WordSolution) => {
      mutatePuzzleBoard((pb) => {
        const new_pb = new PuzzleBoard(pb);
        return new_pb;
      });
    },
  );

  return (
    <GameStateContext.Provider value={game}>
      {props.children}
    </GameStateContext.Provider>
  );
};

export const useGame = () => useContext<Game>(GameStateContext);
