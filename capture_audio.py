def capture_audio():
    """Captures audio for the specified duration."""
    print(f"Recording audio for {DURATION} seconds...")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.float32)
    sd.wait()  # Wait for the recording to finish
    print(f"Captured audio: {audio[:10]}...")  # Print the first few samples
    return audio.flatten()

# Modify the capture_audio function to ensure it's mono channel
def capture_audio():
    """Captures audio for the specified duration."""
    print(f"Recording audio for {DURATION} seconds...")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.float32)
    sd.wait()  # Wait for the recording to finish
    audio = np.mean(audio, axis=1)  # Convert to mono if stereo
    print(f"Captured audio: {audio[:10]}...")  # Debug print
    return audio

def capture_audio():
    """Captures audio for the specified duration and saves it to a file."""
    print(f"Recording audio for {DURATION} seconds...")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype=np.float32)
    sd.wait()  # Wait for the recording to finish
    sd.write("test_audio.wav", audio, SAMPLERATE)  # Save audio to file for debugging
    return audio

def transcribe(audio):
    """Transcribes the captured audio using Whisper."""
    print("Transcribing audio...")
    result = model.transcribe("test_audio.wav", fp16=False)  # Use the saved file for transcription
    print("Transcription:", result["text"])
