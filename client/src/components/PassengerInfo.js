import React from "react";

export default function PassengerInfo() {
    return (
        <div className="passenger-info">
            <label htmlFor="name">Name:</label>
            <input type="text" id="name" name="name" />
            <label htmlFor="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" />
        </div>
    )
}