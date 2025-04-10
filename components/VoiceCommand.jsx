// components/VoiceCommand.jsx

import React, { useEffect, useState } from "react";
import WakeWordListener from "../core/WakeWordListener";

const VoiceCommand = ({ onCommand }) => {
  const [listening, setListening] = useState(false);

  useEffect(() => {
    const listener = new WakeWordListener("gptx");
    listener.init((command) => {
      onCommand(command);
    });
    setListening(true);

    return () => listener.stop();
  }, [onCommand]);

  return (
    <div className="voice-ui">
      <h3>🎙️ Voice Control</h3>
      <p>Status: {listening ? "Listening..." : "Inactive"}</p>
    </div>
  );
};

export default VoiceCommand;
