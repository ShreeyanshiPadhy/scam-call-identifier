import json

with open("scam_keywords.json") as f:
    KEYWORDS = json.load(f)

def rule_score(text):
    text = text.lower()
    score = sum(weight for k, weight in KEYWORDS.items() if k in text)
    return min(score * 6, 100)
