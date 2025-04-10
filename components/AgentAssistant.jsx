// components/AgentAssistant.jsx

import React, { useState } from "react";

const AgentAssistant = () => {
  const [input, setInput] = useState("");
  const [log, setLog] = useState([]);

  const handleQuery = async () => {
    const res = await fetch("/api/assistant", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: input })
    });
    const data = await res.json();
    setLog((prev) => [...prev, { user: input, agent: data.response }]);
    setInput("");
  };

  return (
    <div className="dashboard-container">
      <h2>💬 Agent Assistant</h2>
      <input
        type="text"
        placeholder="Ask the agent anything..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={handleQuery}>Send</button>
      <div className="chat-log">
        {log.map((entry, index) => (
          <div key={index}>
            <p><strong>You:</strong> {entry.user}</p>
            <p><strong>Agent:</strong> {entry.agent}</p>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
};

export default AgentAssistant;
