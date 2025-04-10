import React from 'react';
import ScrollRing from './ScrollRing';
import MoodPulse from './MoodPulse';
import { useMemoryKernel } from '../core/MemoryKernel';

const LivingDashboard = () => {
  const { username, mood } = useMemoryKernel();

  return (
    <div style={{ padding: '20px', borderRadius: '12px', border: '2px solid #aaa' }}>
      <h2>👁️ Living Dashboard</h2>
      <p>Agent Synced With: {username}</p>
      <MoodPulse mood={mood} />
      <ScrollRing />
    </div>
  );
};

export default LivingDashboard;
