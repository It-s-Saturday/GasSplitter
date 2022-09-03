import DriverInfo from "./components/DriverInfo"
import Passengers from "./components/Passengers"
import Nav from "./Nav";
import "./App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

function App() {
  const [amount, setAmount] = useState(0)

  const getAmount = (carMake, carModel, carYear, origin, destination, count) => {
    axios
      .get(`http://localhost:8080/calculate/${carMake}/${carModel}/${carYear}/${origin}/${destination}/${count}`)
      .then((response) => {
        console.log(response);
        if (response.status === 200) {
          setAmount(response.data.value);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const sendMessages = (numbers, message) => {
    axios
      .get(`http://localhost:8080/send/${numbers}/${message}`)
      .then((response) => {
        if (response.status === 200) {
          console.log("sent")
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };
  

  const handleSubmit = () => {
    
    const driverName = document.getElementById("driver-name").value;
    const carMake = document.getElementById("car-make").value;
    const carModel = document.getElementById("car-model").value;
    const carYear = document.getElementById("car-year").value;
    const origin = document.getElementById("origin").value;
    const destination = document.getElementById("destination").value;
    const passengers = document.getElementsByClassName("passenger-info");
    let numbers = []
    let count = 0
    if (passengers) {
      count = passengers.length;
      let temp = document.querySelectorAll(".passenger-info #phone");
      for (let i = 0; i < temp.length; i++) {
        console.log(temp[i].value)
        numbers.push(temp[i].value)
      }
      console.log(numbers)
    }

    getAmount(carMake, carModel, carYear, origin, destination, count);
    // sendMessages(numbers, `Driver: ${driverName}\nFrom: ${origin}\nTo: ${destination}\nAmount Owed: ${amount}`);
  }


  return (
    <div className="App">
      <Nav />
      <DriverInfo />
      <Passengers />
      <button id="submit" onClick={handleSubmit}>Submit</button>
      <div>Amount: {amount}</div>
    </div>
  );
}

export default App;
