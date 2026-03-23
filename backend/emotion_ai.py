def emotion_score(text):
    fear_words = ["urgent", "arrest", "blocked", "legal"]
    count = sum(1 for w in fear_words if w in text.lower())
    return min(count * 20, 100)
