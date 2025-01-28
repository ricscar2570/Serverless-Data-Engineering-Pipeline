import React from "react";
import { Line } from "react-chartjs-2";

const RealTimeChart = ({ data }) => {
  const chartData = {
    labels: data.map((d) => d.timestamp),
    datasets: [
      {
        label: "Valore Sensori",
        data: data.map((d) => d.value),
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 2,
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default RealTimeChart;

