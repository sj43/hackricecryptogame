import React, { Component } from 'react';
// import './common.css';
import './WhatItIs.css';
// import { Parallax } from 'react-scroll-parallax';

export default class AboutUs extends Component {
    render() {
        return (
            <div className="aboutPageWrapper">
                <div className="outside">
                    {/* <div className="vert-line"></div> */}
                    <h1>Our Mission</h1>
                    <p class="big-p">
                    CryptoGame is a game to teach players about <em>cryptocurrency and financial management</em>.
                    </p>
                    <p class="big-p">
                    We believe that everybody should be financially prepared for the future of currency, and we believe that anyone can learn.                  
                    </p>
                    <p class="big-p"></p>
                    <p id="learn-more">
                        <a href="https://github.com/sj43/hackricecryptogame"><u>Try it out.</u></a>
                    </p>
                </div>
            </div>
        )
    }
}
