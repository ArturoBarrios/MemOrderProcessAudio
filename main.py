from fastapi import FastAPI, HTTPException
from fastapi import Request

app = FastAPI()

@app.post("/trigger-audio")
async def trigger_audio(request: Request):
    