import React, { createContext, useContext, useState } from 'react';

const MemoryContext = createContext();

export const useMemoryKernel = () => useContext(MemoryContext);

export const MemoryProvider = ({ children }) => {
  const [username] = useState('Stanley');
  const [mood, setMood] = useState('focused');
  const [presence, setPresence] = useState(true);
  const [memoryLog, setMemoryLog] = useState([]);

  const pushMemory = (entry) => setMemoryLog((prev) => [...prev, entry]);

  return (
    <MemoryContext.Provider value={{
      username, mood, presence, memoryLog, pushMemory, setMood
    }}>
      {children}
    </MemoryContext.Provider>
  );
};
