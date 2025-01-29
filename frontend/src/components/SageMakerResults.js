import React, { useState } from "react";

const SageMakerResults = () => {
  const [data, setData] = useState("");
  const [result, setResult] = useState("");

  const handlePredict = async () => {
    const response = await fetch("your-api-gateway-url", {
      method: "POST",
      body: JSON.stringify({ data: [1.2, 3.4, 5.6, 7.8, 9.0] }),
      headers: { "Content-Type": "application/json" },
    });

    const json = await response.json();
    setResult(JSON.stringify(json, null, 2));
  };

  return (
    <div>
      <h2>Predizione con SageMaker</h2>
      <button onClick={handlePredict}>Esegui Inferenza</button>
      <pre>{result}</pre>
    </div>
  );
};

export default SageMakerResults;
