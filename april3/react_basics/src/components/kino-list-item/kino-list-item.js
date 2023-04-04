import "./kino-list-item.css"

const KinoListItem = ({movieName, viewCount, favourite}) => {
  return (
    <li className={`kino-list-item d-flex justify-content-between ${favourite && 'favourite'}`}>
      <span className="list-group-item-label">{movieName}</span>
      <input type="number" className="list-group-item-input" defaultValue={viewCount} />
      <div>
        <button type="button" className="btn-cookie btn-sm">
          <i className="fas fa-cookie"></i>
        </button>
        <button type="button" className="btn-trash btn-sm">
          <i className="fas fa-trash"></i>
        </button>
        <i className="fas fa-star"></i>
      </div>
    </li>
  )
}

export default KinoListItem