// core/WakeWordListener.js

class WakeWordListener {
    constructor(wakeWord = "gptx") {
      this.wakeWord = wakeWord.toLowerCase();
      this.recognition = null;
    }
  
    init(callback) {
      if (!('webkitSpeechRecognition' in window)) {
        console.error("Speech Recognition not supported.");
        return;
      }
  
      this.recognition = new webkitSpeechRecognition();
      this.recognition.continuous = true;
      this.recognition.interimResults = false;
      this.recognition.lang = 'en-US';
  
      this.recognition.onresult = (event) => {
        for (let i = event.resultIndex; i < event.results.length; i++) {
          const transcript = event.results[i][0].transcript.trim().toLowerCase();
          if (transcript.includes(this.wakeWord)) {
            callback(transcript);
          }
        }
      };
  
      this.recognition.onerror = (event) => {
        console.error("WakeWordListener error:", event.error);
      };
  
      this.recognition.start();
    }
  
    stop() {
      if (this.recognition) this.recognition.stop();
    }
  }
  
  export default WakeWordListener;
  