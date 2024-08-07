#!/usr/bin/python3
""" Module that queries the Reddit API  """
import requests


def top_ten(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {'limit': 10}

    res = requests.get(url, headers=headers,
                       allow_redirects=False, params=params)

    if res.status_code == 200:
        posts = res.json().get('data', {}).get(
            'children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title', {}))
    else:
        print('None')
        return
