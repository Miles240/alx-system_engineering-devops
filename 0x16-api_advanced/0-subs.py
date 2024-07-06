#!/usr/bin/python3
""" Module that queries the Reddit API  """
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json().get('data', {}).get('subscribers')
    else:
        return 0
