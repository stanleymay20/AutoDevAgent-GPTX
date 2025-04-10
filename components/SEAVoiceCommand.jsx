// components/SEAVoiceCommand.jsx
import React, { useEffect } from 'react';
import { streamOpenAIResponse } from '../utils/openai';

export default function SEAVoiceCommand({ onCommand }) {
  useEffect(() => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.lang = 'en-US';

    recognition.onresult = async (event) => {
      const transcript = event.results[event.results.length - 1][0].transcript;
      const response = await streamOpenAIResponse(transcript);
      onCommand(transcript, response);
    };

    recognition.start();
  }, [onCommand]);

  return <div>Listening for S.E.A. Commands...</div>;
}
