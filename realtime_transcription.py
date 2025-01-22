import whisper
import sounddevice as sd
import numpy as np

# Load the Whisper model
model = whisper.load_model("base")

# Define recording parameters
samplerate = 16000  # Sampling rate
duration = 10  # Duration to capture audio in seconds

print("Recording... Speak into the microphone.")

# Record audio
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.float32)
sd.wait()  # Wait for the recording to finish

print("Transcribing...")

# Convert audio to the format expected by Whisper
audio_np = np.squeeze(audio) * 32767  # Convert to 16-bit PCM
audio_bytes = audio_np.astype(np.int16).tobytes()

# Transcribe audio
result = model.transcribe(audio_bytes)

# Output transcription
print("Transcription:")
print(result["text"])

