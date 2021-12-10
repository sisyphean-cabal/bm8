import React, { Component } from "react";
import ReactDOM from 'react-dom'

import HomePage from "./HomePage"
import RegisterPage from "./RegisterPage"
import ProfilePage from "./ProfilePage"
import MessagePage from "./MessagePage"

export default class App extends Component {
    constructor(props){
        super(props)
    }

    render(){
        return (
          <div>
              <HomePage/>
              <RegisterPage/>
              <ProfilePage/>
              <MessagePage/>
          </div>
        );
    }
}

const appDiv = document.getElementById("app")
ReactDOM.render(<App />, appDiv)

