import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path
import datetime

def record_audio(duration=5, samplerate=16000, filename=None):
    """
    Records audio from the default microphone and saves it to a WAV file.
    Compatible with macOS and Raspberry Pi.

    Args:
        duration (int): seconds to record
        samplerate (int): samples per second (16000 is good for speech and Whisper)
        filename (str): optional filename; defaults to timestamped name

    Returns:
        str: path to the saved WAV file
    """
    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"audio_{timestamp}.wav"

    path = Path(filename)

    print(f"Recording for {duration} seconds...")

    try:
        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype='int16'
        )
        sd.wait()
        write(str(path), samplerate, recording)
    except Exception as e:
        print("❌ Recording failed:", e)
        raise

    print(f"Saved recording to {path}")
    return str(path)
