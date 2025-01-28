import React, { useState, useEffect } from "react";
import RealTimeChart from "./RealTimeChart";
import DataGeneratorForm from "./DataGeneratorForm";

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/api/data")
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <DataGeneratorForm />
      <RealTimeChart data={data} />
    </div>
  );
};

export default Dashboard;

