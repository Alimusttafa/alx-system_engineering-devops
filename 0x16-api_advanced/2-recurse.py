#!/usr/bin/python3
"""getsubs

Return: number of subs of a sub
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    hot_list.extend(data['data']['children'])

    after = data['data'].get('after')

    if after:
        recurse(subreddit, hot_list, after)

    return hot_list


if __name__ == "__main__":
    subreddit = 'programming'
    all_posts = recurse(subreddit)
    print(f"Total posts fetched from r/{subreddit}: {len(all_posts)}")
