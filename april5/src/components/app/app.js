import React from 'react'
import "./app.css"

const Item = ({title, date, content, url}) => {
    return (
        <div>
            <a href={url}>
                <h3>{title}</h3>
            </a>
            <p>{date}</p>
            <p>{content} <a href="somewhere.com">read more</a></p>
        </div>
    )
}

const App = () => {
  return (
    <div className='app'>
        <Item title="Maktabgacha Ta'til Haqida" url="jjj.com/awhibfhwe" date="2023/04/05" content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book... " />

        <Item title="Hususiy Korxona tuzish haqida" url="jjj.com/awhibfhwe" date="2023/04/05" content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book... " />
    </div>
  )
}

export default App