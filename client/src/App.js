import DriverInfo from "./components/DriverInfo"
import Passengers from "./components/Passengers"
import Nav from "./Nav";
import "./App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

function App() {
  const [content, setContent] = useState("");
  const [amount, setAmount] = useState(0)

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
      <Nav />
      <DriverInfo />
      <Passengers />
      <button>Submit</button>
      <div>Amount: {amount}</div>
    </div>
  );
}

export default App;
