#!/usr/bin/python3
"""Module that requests the number of subscribers from a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """function that request the total subscribers from a given subreddit
        Returns 0 if the subreddit does not exist
    """
    # Explicitly request JSON format
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Setting a custom User-Agent to comply with Reddit API policy
    headers = {"User-Agent": "Custom"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:  # Check if the request was successful
            data = res.json()  # Parse the response as JSON
            # Ensure the expected keys are in the response
            if "data" in data and "subscribers" in data["data"]:
                # Return the number of subscribers
                return data["data"]["subscribers"]
            else:
                print(f"Unexpected response structure: {data}")
                return 0
        elif res.status_code == 302:  # Check for redirect status
            print(
                f"The subreddit '{subreddit}' does not exist or has been redirected.")
            return 0
        elif (
            res.status_code == 404
        ):  # Explicitly handle the case where the subreddit does not exist
            print(f"The subreddit '{subreddit}' does not exist.")
            return 0
        else:  # Handle other potential status codes
            print(
                f"Failed to fetch subreddit information. Status code: {res.status_code}"
            )
            return 0

    except requests.exceptions.RequestException as e:  # Handle any request exceptions
        print(f"An error occurred: {e}")
        return 0
