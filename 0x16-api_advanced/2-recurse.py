#!/usr/bin/python3
""" Module that queries the Reddit API  """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPI/0.0.2"}
    params = {'after': after}

    res = requests.get(url, headers=headers,
                       allow_redirects=False, params=params)

    if res.status_code == 200:
        after = res.json().get('data').get('after')
        children = res.json().get('data').get('children')
        for child in children:
            data = child.get('data')
            hot_list.append(child.get('title'))

        if after is None:
            return hot_list
        else:
          return  recurse(subreddit, hot_list, after)
    else:
        return None