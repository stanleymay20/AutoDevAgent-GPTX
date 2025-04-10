// core/PresenceMusicController.js

class PresenceMusicController {
    constructor() {
      this.audio = new Audio();
      this.moodTracks = {
        focus: "/static/audio/focus.mp3",
        calm: "/static/audio/calm.mp3",
        alert: "/static/audio/alert.mp3"
      };
    }
  
    playMood(mood = "focus") {
      const track = this.moodTracks[mood] || this.moodTracks["focus"];
      this.audio.src = track;
      this.audio.loop = true;
      this.audio.volume = 0.3;
      this.audio.play().catch(console.error);
    }
  
    stop() {
      this.audio.pause();
      this.audio.currentTime = 0;
    }
  
    setVolume(level) {
      this.audio.volume = Math.max(0, Math.min(1, level));
    }
  }
  
  export default new PresenceMusicController();
  