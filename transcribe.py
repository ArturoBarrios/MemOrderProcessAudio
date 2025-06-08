import whisper


model = whisper.load_model("medium")  # try "tiny" for speed or Pi compatibility

def transcribe_audio(audio_path: str):
    print(f"Transcribing audio at: {audio_path}")
    
    result = model.transcribe(audio_path)
    
    return {
        "transcript": result["text"],
        "confidence": result.get("confidence", 0.9)  # Whisper doesn't always give this
    }
