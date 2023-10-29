import GameSummary from './puzzles/gamesummary';

const Toolbar = (props) => {
  return (
    <div class='w-full bg-blue-700 p-2'>
      <span class=' text-2xl font-bold text-[gold] shadow-lg'>Hunt Words</span>
      <GameSummary />
    </div>
  );
};

export default Toolbar;
