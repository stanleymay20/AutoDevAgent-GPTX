import React, { useEffect } from 'react';
import { useMemoryKernel } from '../core/MemoryKernel';
import { getMoodColor, getAgentTone } from '../utils/personalityUtils';

const AgentPersonalityCore = () => {
  const { username, mood } = useMemoryKernel();
  const tone = getAgentTone(mood);
  const style = { background: getMoodColor(mood), padding: '10px', borderRadius: '10px' };

  useEffect(() => {
    console.log(`[Personality Activated] Mood: ${mood}, Tone: ${tone}`);
  }, [mood]);

  return (
    <div style={style}>
      <h2>Hello, {username}! I’m synced to your vibe.</h2>
      <p>Current Mood: <strong>{mood}</strong></p>
      <p>Tone of interaction: <em>{tone}</em></p>
    </div>
  );
};

export default AgentPersonalityCore;
