import { Puzzle, PuzzleBoard } from './puzzle.model';

const api_url = `${document.location.origin}/api/`;
// const isChromeOS = /\bCrOS\b/.test(navigator.userAgent);

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
  let puzzles: Puzzle[];
  await resp.then((r) => {
    // console.log("in puzzles promise: ", r);
    puzzles = r.body;
  });
  puzzles = puzzles.map((p) => new Puzzle(p)).toSorted(Puzzle.sort_array);

  return puzzles;
};

export const fetchPuzzleBoard = async (
  puzzleName: string,
): Promise<PuzzleBoard> => {
  // console.log('fetchPuzzleBoard: puzzleName: ', puzzleName);
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
    // console.log('in fetchPuzzleBoard promise: ', r);
    board = new PuzzleBoard(r.body.puzzleboard);

    // notify that a puzzle was consumed
    consumePuzzleBoard(board);
  });
  return board;
};

export const consumePuzzleBoard = (
  puzzleboard: PuzzleBoard,
): void => {
  const puzzleName = puzzleboard?.puzzle?.name;

  // console.log('consumePuzzleBoard: puzzleName: ', puzzleName);

  if (!puzzleName) {
    return null;
  }

  const resp = (
    fetch(api_url + 'async/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        oper: 'puzzleboard-consumed',
        body: { puzzle: puzzleName, size: puzzleboard.height },
      }),
      cache: 'no-cache',
      mode: 'same-origin',
    })
  );
  resp.then((r) => {
    // console.log('in consumePuzzleBoard promise: ', r);
  });
};
