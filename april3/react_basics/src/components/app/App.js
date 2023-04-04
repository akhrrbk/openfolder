import './app.css';
import AppInfo from "../app-info/app-info"
import SearchPanel from "../search-panel/search-panel"
import AppFilter from "../app-filter/app-filter"
import KinoList from "../kino_list/kino-list"
import YangiKino from "../yangi-kino/yangi-kino"

function App() {
  const data = [
    {movieName: "The Witch 2: The Other  One", viewCount: 58220, favourite: true, id: 1},
    {movieName: "The Cop, the Ganster, the Devil", viewCount: 4444455, favourite: true, id: 2},
    {movieName: "The Outlaws", viewCount: 456842, favourite: true, id: 3},
    {movieName: "The Blacklist", viewCount: 552554, favourite: true, id: 4},
    {movieName: "O'zbekchalari", viewCount: 5, favourite: false, id: 5}
  ]
  return (
    <div className="app font-monospace">
      <div className='content'>
        <AppInfo />
        <div className='search-filter'>
          <SearchPanel />
          <AppFilter />
        </div>
        <KinoList data={data} />
        <YangiKino />
      </div>
    </div>
  );
}

export default App;
