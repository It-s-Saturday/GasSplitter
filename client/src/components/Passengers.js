import React, { useState } from "react";
import PassengerInfo from "./PassengerInfo";

export default function Passengers() {
    const [riders, setRiders] = useState([])
    const handleAdd = () => {
        setRiders(riders.concat(<PassengerInfo key={riders.length} />))
    }
    const handleRemove = () => {
        let array = [...riders];
        if (array.length !== 0) {
            array.splice(-1);
            setRiders(array);
        }
    }

    return (
        <div>
            <div id="passengers">
                {
                    riders
                }
                <button onClick={handleAdd}>Add Rider</button>
                <button onClick={handleRemove}>Remove Rider</button>
            </div>
        </div>
    )
}