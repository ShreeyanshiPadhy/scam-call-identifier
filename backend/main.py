from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import shutil
import os
import uuid

from risk_engine import final_risk
from live_risk_engine import live_risk
from audio_to_text import transcribe_audio

from pydantic import BaseModel

# -------------------
# App initialization
# -------------------
app = FastAPI(
    title="DhvaniKavach Scam Detection API",
    description="Text, live-call and voice-based scam risk detection",
    version="1.0.0"
)

# -------------------
# CORS configuration
# -------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------
# Request Models
# -------------------
class TextRequest(BaseModel):
    text: str

class LiveRequest(BaseModel):
    chunks: List[str]

class LiveTextRequest(BaseModel):
    text: str


# -------------------
# Routes
# -------------------

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "DhvaniKavach backend running"
    }

# ---- Text-based analysis ----
@app.post("/analyze-text")
def analyze_text(req: TextRequest):
    risk = final_risk(req.text)
    return {
        "risk": risk,
        "message": "Scam risk calculated successfully"
    }

# ---- Live call protection ----
@app.post("/live-analyze")
def live_analyze(req: LiveRequest):
    risk = live_risk(req.chunks)
    alert = risk >= 50   # earlier warning for live calls

    return {
        "risk": risk,
        "alert": alert,
        "message": (
            "🚨 High scam risk detected"
            if alert
            else "Monitoring call, no immediate threat"
        )
    }

# ---- Audio (voice) analysis ----
@app.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):
    import uuid
    import os
    import shutil

    # ✅ preserve correct extension
    ext = os.path.splitext(file.filename)[1]
    if not ext:
        ext = ".webm"

    temp_path = f"temp_{uuid.uuid4().hex}{ext}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = transcribe_audio(temp_path)
        risk = final_risk(text)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return {
        "transcript": text,
        "risk": risk,
        "alert": risk >= 60
    }

# ---- Live text analysis (for testing) ----
@app.post("/live-analyze-text")
def live_analyze_text(req: LiveTextRequest):
    risk = final_risk(req.text)

    return {
        "risk": risk,
        "alert": risk >= 50,
        "message": "Live monitoring"
    }
