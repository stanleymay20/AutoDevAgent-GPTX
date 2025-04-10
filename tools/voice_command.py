import whisper
import os
from pathlib import Path
import sounddevice as sd
import scipy.io.wavfile as wav

AUDIO_FILE = "voice_input.wav"
TASK_FILE = "context/current_task.txt"
DURATION = 10  # seconds
SAMPLERATE = 16000

def record_audio():
    print("🎙️ Recording... Speak your task clearly.")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
    sd.wait()
    wav.write(AUDIO_FILE, SAMPLERATE, audio)
    print("✅ Audio recorded.")

def transcribe_audio():
    model = whisper.load_model("base")
    print("🔍 Transcribing...")
    result = model.transcribe(AUDIO_FILE)
    print("📝 Task:", result['text'])
    with open(TASK_FILE, "w") as f:
        f.write(result['text'])

if __name__ == "__main__":
    record_audio()
    transcribe_audio()
