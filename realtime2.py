import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os
import wave

# Whisper model
model = whisper.load_model("base")

# Function to record audio
def record_audio(duration=5, samplerate=16000):
    print(f"Recording audio for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
    sd.wait()  # Wait for the recording to finish
    return recording

# Function to save audio to a temporary file
def save_audio_to_file(audio, samplerate):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    return temp_file.name

# Main loop for real-time transcription
try:
    while True:
        audio = record_audio()
        temp_file = save_audio_to_file(audio, samplerate=16000)
        
        print("Transcribing audio...")
        result = model.transcribe(temp_file)
        print("Transcription:", result["text"])
        
        os.remove(temp_file)  # Clean up temporary file
except KeyboardInterrupt:
    print("\nStopped listening.")
