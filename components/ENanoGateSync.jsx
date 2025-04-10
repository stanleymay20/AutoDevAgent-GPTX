import React, { useEffect, useState } from 'react';
import { useENanoSync } from '../hooks/useENanoSync';

const ENanoGateSync = () => {
  const { currentGate, solarHour, nextPulse } = useENanoSync();

  return (
    <div style={{ padding: '12px', background: '#222', color: '#fff' }}>
      <h4>🔆 ENano Gate Active: {currentGate}</h4>
      <p>Solar Hour: {solarHour}</p>
      <p>Next Scroll Pulse in: {nextPulse}</p>
    </div>
  );
};

export default ENanoGateSync;
