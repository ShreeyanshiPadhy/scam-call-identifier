import pandas as pd
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# --------- text cleaning ----------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text

# --------- load dataset ----------
df = pd.read_csv("scam_text_dataset.csv")

# 🔥 FIX: strip column name spaces
df.columns = df.columns.str.strip()

print("Columns:", df.columns)

df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["label"]

# --------- NLP pipeline ----------
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        max_features=5000
    )),
    ("clf", MultinomialNB())
])

pipeline.fit(X, y)

# --------- save model ----------
pickle.dump(pipeline, open("advanced_text_model.pkl", "wb"))

print("✅ Advanced NLP scam model trained & saved")
