# reddit_config.py
import praw

reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="sentiment-analyzer by u/yourusername"
)
