"use client";
import { useState, useRef } from "react";

export default function LiveCall() {
  const [risk, setRisk] = useState<number | null>(null);
  const recognitionRef = useRef<any>(null);

  const startListening = () => {
    const SpeechRecognition =
      (window as any).SpeechRecognition ||
      (window as any).webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Speech Recognition not supported");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = true;
    recognition.interimResults = false;

    recognition.onresult = async (event: any) => {
      const transcript =
        event.results[event.results.length - 1][0].transcript;

      console.log("Heard:", transcript);

      const res = await fetch("http://localhost:8000/live-analyze-text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: transcript }),
      });

      const data = await res.json();
      setRisk(data.risk);
    };

    recognition.start();
    recognitionRef.current = recognition;
  };

  const stopListening = () => {
    recognitionRef.current?.stop();
  };

  return (
    <div>
      <h1>Live Scam Call Protection</h1>
      <button onClick={startListening}>Start Call</button>
      <button onClick={stopListening}>Stop Call</button>

      {risk !== null && <h2>Live Risk: {risk}</h2>}
    </div>
  );
}
