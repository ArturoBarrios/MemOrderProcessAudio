import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # this loads your .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(audio_path: str):
    print(f"Transcribing audio at: {audio_path}")

    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return {
        "transcript": response.text        
    }
