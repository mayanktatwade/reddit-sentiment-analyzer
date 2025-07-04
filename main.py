from reddit_config import reddit
from sentiment_utils import get_sentiment, summarize_sentiments
from datetime import datetime

# Get topic from user
topic = input("🔎 Enter a topic to search on Reddit: ")

results = reddit.subreddit("all").search(topic, sort="relevance", time_filter="month", limit=20)

post_sentiments = []
comment_sentiments = []
sentiment_scores = []
i = 1

for post in results:
    if any(word in post.title.lower() for word in ["meme", "joke", "shitpost"]):
        continue
    if not post.selftext and post.num_comments < 3:
        continue

    post_date = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d')
    combined_text = post.title + " " + post.selftext
    post_sentiment, post_score = get_sentiment(combined_text)
    post_sentiments.append(post_sentiment)
    sentiment_scores.append(post_score if post_sentiment == "POSITIVE" else -post_score)

    print(f"\n📌 Post {i}")
    print("📅 Date:", post_date)
    print("🧵 Title:", post.title)
    print("📝 Body:", post.selftext if post.selftext else "[No body]")
    print(f"📈 Sentiment: {post_sentiment} ({post_score:.2f})")

    post.comments.replace_more(limit=0)
    sorted_comments = sorted(post.comments[:10], key=lambda x: x.score, reverse=True)
    top_comments = sorted_comments[:3]

    print("💬 Top Comments:")
    for comment in top_comments:
        sentiment, score = get_sentiment(comment.body)
        comment_sentiments.append(sentiment)
        sentiment_scores.append(score if sentiment == "POSITIVE" else -score)
        print(f" - {comment.body[:100]}... ({sentiment}, {score:.2f})")

    i += 1

print("\n📊 Overall Topic Sentiment Analysis:")
print("\n🧵 Posts:")
post_summary = summarize_sentiments(post_sentiments)

print("\n💬 Comments:")
comment_summary = summarize_sentiments(comment_sentiments)

# Calculate proportion of positive posts and comments
positive_post_ratio = sum(1 for label in post_sentiments if label == "POSITIVE") / len(post_sentiments) if post_sentiments else 0
positive_comment_ratio = sum(1 for label in comment_sentiments if label == "POSITIVE") / len(comment_sentiments) if comment_sentiments else 0

# Calculate weighted positive ratio (70% posts, 30% comments)
weighted_positive_ratio = (0.7 * positive_post_ratio) + (0.3 * positive_comment_ratio)

# Calculate average scores (keeping your original method for reference)
post_scores = [score if label == "POSITIVE" else -score for label, score in zip(post_sentiments, sentiment_scores[:len(post_sentiments)])]
comment_scores = [score if label == "POSITIVE" else -score for label, score in zip(comment_sentiments, sentiment_scores[len(post_sentiments):])]
avg_score = (0.7 * (sum(post_scores)/len(post_scores) if post_scores else 0)) + (0.3 * (sum(comment_scores)/len(comment_scores) if comment_scores else 0))

# New combined decision logic
if weighted_positive_ratio < 0.3:  # Less than 30% positive
    # Strong negative sentiment dominates
    summary = "Overall sentiment is \033[91mstrongly negative\033[0m. Significant concerns are being raised."
    sentiment = "STRONGLY_NEGATIVE"
elif weighted_positive_ratio < 0.5:
    # More negative than positive
    if avg_score < -0.2:
        summary = "Overall sentiment is \033[91mnegative\033[0m. People are generally critical."
        sentiment = "NEGATIVE"
    else:
        summary = "Overall sentiment is \033[93mslightly negative\033[0m. Some concerns mixed with neutral views."
        sentiment = "SLIGHTLY_NEGATIVE"
elif weighted_positive_ratio < 0.7:
    # More positive than negative
    if avg_score > 0.2:
        summary = "Overall sentiment is \033[92mpositive\033[0m. Generally favorable views."
        sentiment = "POSITIVE"
    else:
        summary = "Overall sentiment is \033[93mslightly positive\033[0m. Mostly neutral with some optimism."
        sentiment = "SLIGHTLY_POSITIVE"
else:
    # Strong positive sentiment (70%+ positive)
    summary = "Overall sentiment is \033[92mstrongly positive\033[0m. Overwhelmingly optimistic views."
    sentiment = "STRONGLY_POSITIVE"

print(f"\n📊 Overall Topic Sentiment Analysis:")
print(f"\n🧵 Posts:")
print(f"POSITIVE: {sum(1 for label in post_sentiments if label == 'POSITIVE')} ({positive_post_ratio*100:.1f}%)")
print(f"NEGATIVE: {sum(1 for label in post_sentiments if label == 'NEGATIVE')} ({(1-positive_post_ratio)*100:.1f}%)")

print(f"\n💬 Comments:")
print(f"POSITIVE: {sum(1 for label in comment_sentiments if label == 'POSITIVE')} ({positive_comment_ratio*100:.1f}%)")
print(f"NEGATIVE: {sum(1 for label in comment_sentiments if label == 'NEGATIVE')} ({(1-positive_comment_ratio)*100:.1f}%)")

print(f"\n📈 Weighted Positive Ratio: {weighted_positive_ratio:.3f}")
print(f"📊 Average Sentiment Score: {avg_score:.3f}")
print(f"\n📝 Summary: {summary}")
