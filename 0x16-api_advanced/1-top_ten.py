#!/usr/bin/python3
"""
Top Ten
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    headers = {
        "User-Agent": "0x16-api_advanced:project: v1.0.0"
    }

    params = {
        "limit": 10
    }

    res = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

    if res.status_code != 200:
        print(None)

    posts = res.json().get("data", {}).get("children", [])

    for post in posts:
        print(post.get("data", []).get("title"))
