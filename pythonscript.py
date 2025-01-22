import sounddevice as sd
import numpy as np

# Test recording audio for 5 seconds
duration = 5  # seconds
sample_rate = 16000  # samples per second
channels = 1  # mono audio

print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
sd.wait()  # Wait until recording is finished

print("Recording complete.")
print("Audio data:", audio_data)


import whisper
import sounddevice as sd
import numpy as np
import queue

# Initialize the model
model = whisper.load_model("base")

# Define parameters
duration = 5  # seconds
sample_rate = 16000  # samples per second
channels = 1  # mono audio

# Create a queue to store the audio
audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    """This function will be called to record the audio in real-time."""
    if status:
        print(status)
    audio_queue.put(indata.copy())

# Start recording
with sd.InputStream(callback=callback, channels=channels, samplerate=sample_rate):
    print("Listening for audio...")
    while True:
        if not audio_queue.empty():
            audio_data = audio_queue.get()
            # Save audio data as a temporary file
            audio_file = "temp_audio.wav"
            sd.write(audio_file, audio_data, sample_rate)
            
            # Transcribe audio using Whisper
            result = model.transcribe(audio_file)
            print("Transcription:", result["text"])


import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe an existing audio file
audio_file = "test_audio.wav"  # Replace with your file path
result = model.transcribe(audio_file)
print("Transcription:", result["text"])
