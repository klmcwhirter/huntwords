import { Puzzle, PuzzleBoard } from './puzzle.model';

const api_url = `${document.location.origin}/api/`;

export const fetchPuzzles = async (): Promise<Puzzle[]> => {
  const resp = (
    await fetch(api_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ oper: 'puzzles', body: {} }),
      cache: 'no-cache',
      mode: 'same-origin',
    })
  ).json();
  let puzzles;
  await resp.then((r) => {
    // console.log("in puzzles promise: ", r);
    puzzles = r.body;
  });
  return puzzles;
};

export const fetchPuzzleBoard = async (
  puzzleName: string,
): Promise<PuzzleBoard> => {
  //   console.log("fetchPuzzleBoard: puzzleName: ", puzzleName);
  if (!puzzleName) {
    return null;
  }

  const resp = (
    await fetch(api_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        oper: 'puzzleboard-pop',
        body: { puzzle: puzzleName },
      }),
      cache: 'no-cache',
      mode: 'same-origin',
    })
  ).json();
  let board: PuzzleBoard;
  await resp.then((r) => {
    // console.log("in puzzleboard promise: ", r);
    board = new PuzzleBoard(r.body.puzzleboard);
    board.wordsToGo = board.puzzle.words.length;
  });
  return board;
};
