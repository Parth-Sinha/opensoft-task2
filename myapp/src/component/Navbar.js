import React from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';

export default function Navbar() {
    return (
        <div className='navbar'>
            <div className='logo'>
                <h3>
                    <Link to='/'>Website</Link>
                </h3>
            </div>
            <div className='Nav'>

                <ul className='navul'>
                    <li className='navli'>
                        <Link to='/home'>Home</Link>
                    </li>
                    <li className='navli'>
                        <Link to='/page1'>Page1</Link>
                    </li>
                    <li className='navli'>
                        <Link to='/page2'>Page2</Link>

                    </li>
                    <li className='navli'>
                        <Link to='/page3'>Page3</Link>

                    </li>
                </ul>
            </div>

        </div>
    )
}
