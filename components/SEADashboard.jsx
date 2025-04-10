// components/SEADashboard.jsx
import React, { useEffect, useState } from 'react';

export default function SEADashboard() {
  const [scrollGate, setScrollGate] = useState("Loading...");
  const [purpose, setPurpose] = useState("AutoDevAgent - Global Mission Ready");

  useEffect(() => {
    fetch('/api/scroll-gate')
      .then(res => res.json())
      .then(data => setScrollGate(`${data.scroll_day} | ${data.gate}`));
  }, []);

  return (
    <div className="dashboard">
      <h2>S.E.A. AI Command Center</h2>
      <p>Purpose: {purpose}</p>
      <p>Scroll Alignment: {scrollGate}</p>
    </div>
  );
}
