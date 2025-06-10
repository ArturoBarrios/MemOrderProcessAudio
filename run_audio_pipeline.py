from record import record_audio
from vad import apply_vad
from transcribe import transcribe_audio  # you'll mock or build this soon

def main():
    print("Starting audio processing pipeline...")

    audio_path = record_audio()
    print(f"Recorded audio: {audio_path}")

    speech_only_path = apply_vad(audio_path)
    print(f"VAD cleaned audio saved to: {speech_only_path}")

    result = transcribe_audio(speech_only_path)
    print(f"Transcript: {result['transcript']} ")

if __name__ == "__main__":
    main()
