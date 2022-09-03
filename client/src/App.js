import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

function App() {
  const [content, setContent] = useState("");

  useEffect(() => {
    getHello();
  }, []);

  const getHello = () => {
    axios
      .get("http://localhost:8080/hello")
      .then((response) => {
        console.log(response);
        if (response.status === 200) {
          setContent(response.data.text);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        {content}
      </header>
    </div>
  );
}

export default App;
