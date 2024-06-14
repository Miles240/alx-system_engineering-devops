#!/usr/bin/python3
""" Module that queries the Reddit API  """
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}

    res = requests.get(url, headers, allow_redirects=False)

    if res.status_code == 404:
        return 0
    return res.json().get("data").get("subscribers")
