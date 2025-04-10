// components/EmotionDetector.jsx

import React, { useEffect, useState } from "react";

const EmotionDetector = () => {
  const [emotion, setEmotion] = useState("neutral");

  useEffect(() => {
    // Simulated emotion polling (can be replaced with real emotion detection)
    const emotions = ["happy", "sad", "angry", "focused", "excited"];
    const interval = setInterval(() => {
      const randomEmotion = emotions[Math.floor(Math.random() * emotions.length)];
      setEmotion(randomEmotion);
    }, 10000); // every 10 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="emotion-box">
      <h3>🧠 Detected Emotion: <span>{emotion}</span></h3>
    </div>
  );
};

export default EmotionDetector;
