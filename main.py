from fastapi import FastAPI, HTTPException, Request
from run_audio_pipeline import process_audio_pipeline
import threading

app = FastAPI()

@app.post("/trigger-audio")
async def trigger_audio(request: Request):
    def run_pipeline():
        try:
            process_audio_pipeline()
        except Exception as e:
            print(f"[ERROR] Audio pipeline failed: {e}")

    threading.Thread(target=run_pipeline).start()
    return {"message": "audio service triggered"}
