// components/LiveStudio.jsx

import React, { useState } from "react";

const LiveStudio = () => {
  const [task, setTask] = useState("");
  const [response, setResponse] = useState("Waiting for command...");

  const executeTask = async () => {
    const res = await fetch("/api/execute", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task })
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="dashboard-container">
      <h2>🎛️ Live Studio</h2>
      <textarea
        placeholder="Type a task or prompt"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button onClick={executeTask}>Run</button>

      <div className="response-box">
        <h3>🧠 Agent Response</h3>
        <pre>{response}</pre>
      </div>
    </div>
  );
};

export default LiveStudio;
