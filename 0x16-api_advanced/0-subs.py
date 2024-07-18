#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Number of Subreddit Subscribers
    Keyword arguments:
    subreddit -- the subreddit to check e.g programming.
    Return: the number of subscribers or 0 if the subreddit doesn't exist
    """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) \
                Gecko/20100101 Firefox/90.0'
        }
        reddit_request = requests.get(url,
                                      headers=headers,
                                      allow_redirects=False)
        reddit_json = reddit_request.json()
        return reddit_json.get('data').get('subscribers')
    except requests.JSONDecodeError as e:
        return (0)
    except Exception as e:
        return (0)
