import BoardSummary from './boardsummary';
import BoardCellsView from './boardcells';

const PuzzleBoardView = (props) => {
  return (
    <div class='mt-0 grid h-[94vh] grow grid-cols-3 gap-4 bg-blue-200 p-2 p-2 align-top'>
      <BoardCellsView />
      <BoardSummary />
    </div>
  );
};

export default PuzzleBoardView;
