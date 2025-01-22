import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile

# Load Whisper model
model = whisper.load_model("base")  # Choose 'tiny', 'small', etc., as needed

# Audio configuration
SAMPLERATE = 16000  # Whisper requires 16kHz
DURATION = 20  # Duration to capture audio in seconds

def capture_audio():
    """Captures audio for the specified duration."""
    print(f"Recording audio for {DURATION} seconds...")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.float32)
    sd.wait()  # Wait for the recording to finish
    print(f"Captured audio data (first 10 samples): {audio[:10]}...")
    # Save audio to a file for debugging
    wavfile.write("test_audio.wav", SAMPLERATE, (audio * 32767).astype(np.int16))
    return audio

def transcribe(audio):
    """Transcribes the captured audio using Whisper."""
    print("Transcribing audio from the saved file...")
    result = model.transcribe("test_audio.wav", fp16=False)  # Use the saved file for transcription
    print("Transcription:", result["text"])

try:
    print("Listening for audio...")
    while True:
        audio = capture_audio()
        transcribe(audio)
except KeyboardInterrupt:
    print("\nStopped listening.")
except Exception as e:
    print(f"An error occurred: {e}")
