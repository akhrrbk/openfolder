import './app.css';
import AppInfo from "../app-info/app-info"
import SearchPanel from "../search-panel/search-panel"
import AppFilter from "../app-filter/app-filter"
import KinoList from "../kino_list/kino-list"
import YangiKino from "../yangi-kino/yangi-kino"

function App() {
  return (
    <div className="app font-monospace">
      <div className='content'>
        <AppInfo />
        <div className='search-filter'>
          <SearchPanel />
          <AppFilter />
        </div>
        <KinoList />
        <YangiKino />
      </div>
    </div>
  );
}

export default App;
