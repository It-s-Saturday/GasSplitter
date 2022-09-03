import React from "react";
import "./DriverInfo.css"

export default function DriverInfo() {
    return (
        <div className="container">
            <h4>Driver</h4>
            <label htmlFor="driver-name">Driver Name:</label>
            <input type="text" id="driver-name" name="driver-name" required />
            <label htmlFor="car-make">Car Make:</label>
            <input type="text" id="car-make" name="make" required />
            <label htmlFor="car-model">Car Model:</label>
            <input type="text" id="car-model" name="car-model" required />
            <label htmlFor="name">Car Year:</label>
            <input type="number" id="car-year" name="car-year" required />
            <label htmlFor="origin">Origin:</label>
            <input type="text" id="origin" name="origin" required/>
            <label htmlFor="destination">Destination:</label>
            <input type="text" id="destination" name="name" required />
        </div>
    )
}