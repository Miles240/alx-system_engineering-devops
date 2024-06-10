import praw

# Create a Reddit instance
reddit = praw.Reddit(
    client_id="nlOpORtYC8UH7JblzSFYeA",
    client_secret="NgmFtp-5Sg4MgFsvlcqesowvVOalQQ",
    user_agent="Miles/0.0.1 by bg_miles",
)

# Get the top 10 hot posts from the Python subreddit
subreddit = reddit.subreddit("Python")
for submission in subreddit.hot(limit=10):
    print(f"Title: {submission.title}, Upvotes: {submission.score}")
