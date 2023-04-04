import "./kino-list.css"
import KinoListItem from "../kino-list-item/kino-list-item"

const KinoList = ({data}) => {
  return (
    <ul className="kino-list">
      {data.map(item => (
        <KinoListItem key={item.id} {...item} />
        // <KinoListItem key={item.id} movieName={item.movieName} viewCount={item.viewCount} favourite={item.favourite} />
      ))}
    </ul>
  )
}

export default KinoList