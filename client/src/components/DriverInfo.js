import React from "react";

export default function DriverInfo() {
    return (
        <div>
            <label htmlFor="driver-name">Name:</label>
            <input type="text" id="driver-name" name="driver-name" />
            <label htmlFor="car-name">Car Name:</label>
            <input type="text" id="name" name="name" />
            <label htmlFor="car-model">Car Model:</label>
            <input type="text" id="car-model" name="car-model" />
            <label htmlFor="name">Car Year:</label>
            <input type="number" id="car-year" name="car-year" />
            <label htmlFor="origin">Origin:</label>
            <input type="text" id="origin" name="origin" />
            <label htmlFor="destination">Destination:</label>
            <input type="text" id="destinatio" name="name" />
        </div>
    )
}