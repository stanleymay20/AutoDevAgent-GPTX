import { MemoryProvider } from './core/AutoDevAgentKernel';
import AgentPersonalityCore from './components/AgentPersonalityCore';
import ConversationalMemoryCore from './components/ConversationalMemoryCore';
import LivingDashboard from './components/LivingDashboard';
import VoicePresenceAura from './components/VoicePresenceAura';
import ENanoGateSync from './components/ENanoGateSync';

function App() {
  return (
    <MemoryProvider>
      <VoicePresenceAura />
      <ENanoGateSync />
      <LivingDashboard />
      <AgentPersonalityCore />
      <ConversationalMemoryCore />
    </MemoryProvider>
  );
}
