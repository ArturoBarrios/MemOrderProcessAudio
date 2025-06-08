import torch
import numpy as np
from pydub import AudioSegment
from pathlib import Path

def apply_vad(audio_path: str, output_path: str = "speech_only.wav", threshold: float = 0.5):
    """
    Applies VAD to the input audio and returns a single cleaned .wav file with only speech.
    """
    # Load and standardize audio
    audio = AudioSegment.from_file(audio_path)
    sample_rate = 16000
    audio = audio.set_channels(1).set_frame_rate(sample_rate)

    samples = np.array(audio.get_array_of_samples(), dtype=np.float32) / 32768.0

    # Load Silero VAD model
    model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad', model='silero_vad', force_reload=False)
    get_speech_ts = utils[0]

  

    speech_timestamps = get_speech_ts(samples, model, sampling_rate=sample_rate)

    # Combine all speech segments
    speech_audio = AudioSegment.silent(duration=0)
    for ts in speech_timestamps:
        start_ms = int(1000 * ts['start'] / sample_rate)
        end_ms = int(1000 * ts['end'] / sample_rate)
        speech_audio += audio[start_ms:end_ms]

    # Export the combined speech-only audio
    speech_audio.export(output_path, format="wav")

    return output_path
