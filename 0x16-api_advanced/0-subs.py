#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""

    url = f'http://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        'User-Agent': '0x16-api_advanced:project: v1.0.0'
    }

    res = requests.get(
            url,
            headers,
            allow_redirects=False
        )

    if res.status_code != 200:
        return 0

    return res.json().get("data", {}).get("subscribers", 0)
