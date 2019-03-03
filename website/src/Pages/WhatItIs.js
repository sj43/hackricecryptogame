import React, { Component } from 'react';
// import './common.css';
import './WhatItIs.css';
// import { Parallax } from 'react-scroll-parallax';

export default class AboutUs extends Component {
    render() {
        return (
            <div className="AboutPageWrapper">
                <div className="outside">
                    {/* <div className="vert-line"></div> */}
                    <p id="big-p">
                    CryptoGame is a cryptocurrency trading game using python to teach players about 8 , We will also have quests that the players can perform to gain extra points at the end of the game.
                    </p>
                    <p id="learn-more">
                        <a href="https://www.google.com/"><u>Here's our mission.</u></a>
                    </p>
                </div>
            </div>
        )
    }
}
