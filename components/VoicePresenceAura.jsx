import React, { useEffect } from 'react';
import { useMemoryKernel } from '../core/MemoryKernel';

const VoicePresenceAura = () => {
  const { presence, mood } = useMemoryKernel();

  useEffect(() => {
    const sound = new Audio(`/audio/auras/${mood}.mp3`);
    if (presence) sound.play();
  }, [presence, mood]);

  return null; // Just runs aura effects
};

export default VoicePresenceAura;
