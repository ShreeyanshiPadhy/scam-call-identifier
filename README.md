# DhvaniKavach – Real-Time Scam Call Detection System

🚧 **Status: Work in Progress (WIP)**  
This project is currently under active development. Features, architecture, and documentation may change as the system evolves.

An AI-powered system that detects fraudulent or scam phone calls in real time using speech recognition and machine learning. The system analyzes live or recorded audio, identifies scam-related linguistic patterns, and generates a risk score to warn users before financial or personal data loss occurs.

---

## 🎯 Project Overview

Phone-based scams are rapidly increasing, often targeting elderly and vulnerable individuals. Most fraud detection tools identify scams **after the damage has already occurred**.

**DhvaniKavach** focuses on **proactive prevention** by analyzing call audio and language patterns in real time.

The system:

* Captures live microphone audio or recorded calls
* Converts speech to text using AI speech recognition
* Detects scam keywords and linguistic patterns
* Applies machine learning classification
* Generates a real-time **scam risk score**
* Alerts users when suspicious activity is detected

---

## ⚙️ System Architecture

1. User provides live microphone input or uploads an audio file
2. Audio is streamed or sent to the backend in chunks
3. Speech-to-text converts audio into text using Whisper models
4. Text is analyzed using:

   * Machine Learning classifier
   * Rule-based scam keyword detection
5. Risk engine calculates a **scam probability score**
6. Frontend displays alerts and warnings instantly

---

## 🧠 Core Features

* 🎙 **Real-Time Audio Processing** using Web Audio APIs
* 🗣 **Speech-to-Text Transcription** using Whisper / Faster-Whisper
* 🤖 **Machine Learning Classification** using TF-IDF + Logistic Regression
* ⚠ **Scam Keyword Detection** using rule-based pattern analysis
* 📊 **Risk Scoring Engine** combining ML predictions and heuristic rules
* 🚨 **Instant User Alerts** for high-risk calls

---

## 🛠 Tech Stack

### Frontend

* Next.js (React)
* Web Audio API
* MediaRecorder API

### Backend

* FastAPI (Python)

### AI / Machine Learning

* Whisper / Faster-Whisper (Speech-to-Text)
* TF-IDF + Logistic Regression (Text Classification)
* Rule-Based Scam Detection
* Risk Scoring Engine

---

## 📁 Project Structure

```
dhvanikavach/

backend/
├── main.py
├── audio_to_text.py
├── live_stt.py
├── risk_engine.py
├── ml_detector.py
└── requirements.txt

frontend/
├── app/
│   ├── page.tsx
│   ├── layout.tsx
│   └── components/
└── README.md
```

---

## 🚀 Quick Start

### 1️⃣ Install Dependencies

#### Backend

```
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run backend:

```
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

#### Frontend

```
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🧪 Usage

1. Open the application in **Google Chrome**
2. Allow microphone access
3. Speak or simulate a phone call
4. The system will:

* Transcribe speech in near real time
* Analyze the conversation
* Generate a **scam risk score**
* Display alerts if suspicious patterns are detected

---

## 🌐 Browser Compatibility

Currently supported:

* Google Chrome

This is due to the reliance on **Web Speech API and MediaRecorder APIs**, which are most stable in Chrome.

Future updates will add support for:

* Microsoft Edge
* Firefox
* Safari

---

## 📈 Future Enhancements

* Multilingual scam detection
* Speaker sentiment and intent modeling
* Mobile app integration
* Telecom-level API integration
* Continuous learning from new scam patterns
* On-device inference for improved privacy

---

## 🎥 Demo

2-Minute Demonstration Video

[https://drive.google.com/file/d/19IXjkVUIvAo6NYlNTJSskUaIju92HC06/view](https://drive.google.com/file/d/19IXjkVUIvAo6NYlNTJSskUaIju92HC06/view)

---

## 📊 Presentation

Project Presentation Slides

[https://docs.google.com/presentation/d/1JZ4V_n91eehlsHF_gClox46n6qEKFNfM](https://docs.google.com/presentation/d/1JZ4V_n91eehlsHF_gClox46n6qEKFNfM)

---

## 👥 Team

Team Name: **CrankerHunters**

---

## 🎓 Educational Purpose

This project demonstrates how **AI, speech recognition, and machine learning** can be used to build real-time fraud prevention systems.

It is suitable for learning about:

* Real-time audio processing
* Speech recognition pipelines
* ML-based text classification
* Fraud detection systems
* Full-stack AI applications

---

## 🛡 Conclusion

DhvaniKavach shows how AI can act as a **real-time protective layer against phone-based fraud**. By combining speech recognition, machine learning, and rule-based analysis, the system provides early warnings that can help prevent irreversible financial or personal losses.

---

## 📝 License

This project is created for **educational and research purposes**.

---

### For your **resume**, add this project like this:

**DhvaniKavach – Real-Time Scam Call Detection System**
Next.js, FastAPI, Whisper AI, Machine Learning

• Built an **AI-powered system to detect scam calls in real time** using speech recognition and language analysis
• Implemented **speech-to-text transcription using Whisper models** to process live audio streams
• Developed ML classifier using **TF-IDF + Logistic Regression** to identify scam-related linguistic patterns
• Designed a **risk scoring engine combining ML predictions and rule-based detection** to generate fraud alerts

---

If you want, I can also help you **turn your GitHub profile into a recruiter-ready portfolio** (this increases chances in hackathons and internships a lot).
