from collections import Counter
from transformers import pipeline

# Load BERT sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]  # Truncate to 512 tokens
    return result['label'], result['score']


def summarize_sentiments(sentiments):
    counts = Counter(sentiments)
    total = sum(counts.values())
    for label in ["POSITIVE", "NEGATIVE"]:
        print(f"{label}: {counts[label]} ({(counts[label]/total)*100:.1f}%)")
    return counts
