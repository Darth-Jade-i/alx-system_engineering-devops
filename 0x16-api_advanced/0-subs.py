import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit

    Returns:
    int: The number of subscribers, or 0 if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

# Example usage
print(number_of_subscribers('python'))  # Should return the number of subscribers to the 'python' subreddit
print(number_of_subscribers('nonexistent_subreddit'))  # Should return 0
