import pickle
import os

# Always resolve paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "text_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

def ml_score(text: str) -> int:
    vec = vectorizer.transform([text])
    prob = model.predict_proba(vec)[0][1]
    return int(prob * 100)
