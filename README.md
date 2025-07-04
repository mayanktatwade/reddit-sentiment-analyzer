# 🔍 Reddit Sentiment Analyzer with BERT
A powerful NLP tool that analyzes public sentiment on Reddit discussions using BERT models.

## 🌟 Features

- Real-time sentiment analysis of Reddit posts and comments
- BERT-based NLP for accurate sentiment detection
- Automatic filtering of low-quality content (memes, jokes, etc.)
- Weighted sentiment scoring (70% posts, 30% comments)
- Clear visual output with color-coded results

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or later
- Reddit API credentials

### Installation
1. Clone the repository:
```bash
git clone https://github.com/mayanktatwade/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```
2. Install requirements
```bash
pip install -r requirements.txt
```
3. Set Up Reddit API
- Go to (https://www.reddit.com/prefs/apps)
- Click “Create App”
- Choose Script

-Fill details:
  Name: Reddit Sentiment App
  Redirect URI: http://localhost
  
-Copy your:
  client_id, client_secret and user_agent (e.g., sentiment-analyzer by u/yourusername)

4. Configure Reddit Auth
Update reddit_config.py with the help of data from previous step.
