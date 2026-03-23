from ml_detector import ml_score

# simple rolling risk (average of chunks)
def live_risk(chunks: list[str]) -> int:
    if not chunks:
        return 0

    scores = [ml_score(chunk) for chunk in chunks]
    return int(sum(scores) / len(scores))