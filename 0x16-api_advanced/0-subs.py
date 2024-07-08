#!/usr/bin/python3
""" Module that queries the Reddit API  """
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        return res.json().get('data', {}).get('subscribers', 0)
    except requests.RequestException as e:
        return 0
