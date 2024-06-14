#!/bin/bash/python3
""" Module that queries the Reddit API  """
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://oauth.reddit.com/r/{subreddit}/about"
    headers = {"User-Agent": "Custom"}

    res = requests.get(url, headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    return 0
