# 🔍 Reddit Sentiment Analyzer with BERT

A powerful NLP tool that analyzes public sentiment on Reddit discussions using BERT models.

## 🌟 Features

- **Real-time sentiment analysis** of Reddit posts and comments
- **BERT-based NLP** for accurate sentiment detection
- **Automatic filtering** of low-quality content (memes, jokes, etc.)
- **Weighted sentiment scoring** (70% posts, 30% comments)
- **Clear visual output** with color-coded results


## 🚀 Quick Start

### Prerequisites

- Python 3.7 or later
- Reddit API credentials


### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/mayanktatwade/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```

2. **Install requirements:**

```bash
pip install -r requirements.txt
```

3. **Set Up Reddit API:**
    - Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
    - Click **Create App**
    - Choose **Script**
    - Fill details:
        - **Name:** Reddit Sentiment App
        - **Redirect URI:** http://localhost
    - Copy your:
        - `client_id`
        - `client_secret`
        - `user_agent` (e.g., `sentiment-analyzer by u/yourusername`)
4. **Configure Reddit Auth:**
    - Update `reddit_config.py` with the credentials from the previous step.

## 🧠 How It Works

- Searches Reddit using `praw` with filters (last month, relevance)
- Filters out joke posts and low-engagement threads
- Applies HuggingFace transformers sentiment model (`distilbert-base-uncased-finetuned-sst-2-english`)
- Aggregates and weights sentiment using:
    - **Post sentiment:** 70%
    - **Comment sentiment:** 30%
    - Model confidence scores
- Generates a final qualitative summary


## 📈 Summary Levels

| Weighted Positive Ratio | Sentiment Summary |
| :-- | :-- |
| ≥ 0.7 | Strongly Positive |
| 0.5 – 0.7 | Slightly Positive/Positive |
| 0.3 – 0.5 | Slightly Negative/Negative |
| < 0.3 | Strongly Negative |

## 🛡 Security Notes

- ✅ Keep your `client_secret` and `client_id` safe.
- ✅ Use `.gitignore` to prevent pushing credentials to GitHub.
- ❌ Never share your raw `reddit_config.py` publicly.


## 💡 Ideas for Future Work

- Add topic trend visualization using matplotlib or plotly
- Make it a web app using Flask or Streamlit
- Extend to Twitter, Hacker News, YouTube APIs
- Export analysis to `.csv` or `.pdf`


## 🧑‍💻 Author

**Mayank Tatwade**
📬 Email: mayanktatwadeiitb@gmail.com
🔗 GitHub: [@mayanktatwade](https://github.com/mayanktatwade)

## ⭐️ Star This Project

If you found this useful or interesting, please ⭐️ the repo to show support!

