from record import record_audio
from vad import apply_vad
from transcribe import transcribe_audio  # you'll mock or build this soon

def process_audio_pipeline():
    print("Starting audio processing pipeline...")

    audio_path = record_audio()
    print(f"Recorded audio: {audio_path}")

    speech_only_path = apply_vad(audio_path)
    print(f"VAD cleaned audio saved to: {speech_only_path}")

    result = transcribe_audio(speech_only_path)
    print(f"Transcript: {result['transcript']}")

    return result
