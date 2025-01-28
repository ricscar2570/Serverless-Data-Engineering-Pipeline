import React, { useState } from "react";

const DataGeneratorForm = () => {
  const [deviceID, setDeviceID] = useState("");
  const [value, setValue] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/api/data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ device_id: deviceID, value: parseFloat(value) }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Device ID:</label>
        <input
          type="text"
          value={deviceID}
          onChange={(e) => setDeviceID(e.target.value)}
        />
      </div>
      <div>
        <label>Value:</label>
        <input
          type="number"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
      </div>
      <button type="submit">Invia Dati</button>
    </form>
  );
};

export default DataGeneratorForm;

