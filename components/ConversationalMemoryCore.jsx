import React, { useState, useEffect } from 'react';
import { useMemoryKernel } from '../core/MemoryKernel';

const ConversationalMemoryCore = () => {
  const { memoryLog, pushMemory } = useMemoryKernel();
  const [input, setInput] = useState('');

  const handleSubmit = () => {
    pushMemory({ type: 'chat', content: input });
    setInput('');
  };

  return (
    <div style={{ padding: '10px' }}>
      <h3>Conversation Memory</h3>
      <textarea value={input} onChange={(e) => setInput(e.target.value)} rows="3" />
      <button onClick={handleSubmit}>Remember This</button>
      <ul>
        {memoryLog.slice(-5).map((mem, i) => <li key={i}>{mem.content}</li>)}
      </ul>
    </div>
  );
};

export default ConversationalMemoryCore;
