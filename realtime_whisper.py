import whisper
import sounddevice as sd
import numpy as np

# Load Whisper model
model = whisper.load_model("base")  # Choose 'tiny', 'small', etc., as needed

# Audio configuration
SAMPLERATE = 16000  # Whisper requires 16kHz
DURATION = 5  # Duration to capture audio in seconds

def capture_audio():
    """Captures audio for the specified duration."""
    print(f"Recording audio for {DURATION} seconds...")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.float32)
    sd.wait()  # Wait for the recording to finish
    return audio.flatten()

def transcribe(audio):
    """Transcribes the captured audio using Whisper."""
    print("Transcribing audio...")
    result = model.transcribe(audio, fp16=False)  # Use fp16=True for GPU
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

# Assuming you are using the Whisper model like this:
import whisper

model = whisper.load_model("base")
audio = whisper.load_audio("path_to_audio_file.wav")
result = model.transcribe(audio)
print(result['text'])

checkpoint = torch.load(fp, map_location=device, weights_only=True)


# Change the number of seconds to record for
record_duration = 10  # 10 seconds

print("Audio Data:", audio_data)  # or however the data is captured in your script


import whisper

model = whisper.load_model("base")
result = model.transcribe("audio_file_path.wav")
print(result["text"])
