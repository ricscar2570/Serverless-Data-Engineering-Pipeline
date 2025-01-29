import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [pipelineStatus, setPipelineStatus] = useState("...");

  useEffect(() => {
    const fetchStatus = async () => {
      const response = await axios.get("https://your-api-gateway-url/status");
      setPipelineStatus(response.data.status);
    };
    fetchStatus();
  }, []);

  return (
    <div>
      <h1>Serverless Data Pipeline</h1>
      <p>Stato della pipeline: {pipelineStatus}</p>
    </div>
  );
};

export default Dashboard;
