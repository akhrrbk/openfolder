import './yangi-kino.css'

const YangiKino = () => {
  return (
    <div className='yangi-kino'>
      <h3>Yangi Kino Qo'shish</h3>
      <form className='add-form d-flex'>
        <input type="text" className='form-control new-post-label' placeholder='Qanday Kino?' />
        <input type="number" className='form-control new-post-label' placeholder="Nechi Marotaba Ko'rilgan" />
        <button type='submit' className='btn btn-outine-dark'>Qo'shish</button>
      </form>
    </div>
  )
}

export default YangiKino