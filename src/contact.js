import React from 'react'
import { render } from 'react-dom'
import './style.css'
const Contact = () => {
    return (
        <div>
            <h1>Contact webpack</h1>
            <div id="image"></div>
        </div>
    )
}

render( 
    <Contact />,
    document.getElementById('target')
)