# test_vad.py

from vad import apply_vad

if __name__ == "__main__":
    cleaned_audio = apply_vad("test_order.wav")
    print(f"Cleaned audio saved to: {cleaned_audio}")
