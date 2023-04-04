import "./kino-list.css"
import KinoListItem from "../kino-list-item/kino-list-item"

const KinoList = () => {
  return (
    <div className="kino-list">
      KinoList:
      <KinoListItem />
      <KinoListItem />
      <KinoListItem />
      <KinoListItem />
    </div>
  )
}

export default KinoList