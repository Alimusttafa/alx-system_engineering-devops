#!/usr/bin/python3
"""
task 100
"""


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Count the occurrences of words from a given word list in the titles of the
     hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        counts (Counter, optional): A Counter object to store the word counts.
         Defaults to None.
        after (str, optional): A token to paginate through the posts. Defaults
         to None.

    Returns:
        None

    """

    from collections import Counter
    import requests

    if counts is None:
        counts = Counter()

    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    after = data['data'].get('after')

    titles = ' '.join(post['data']['title'].lower()
                      for post in data['data']['children'])
    counts.update(word for word in word_list if word in titles.split())

    if after is not None:
        count_words(subreddit, word_list, counts, after)
    else:
        for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word}: {count}")


if __name__ == "__main__":
    count_words('programming', ['python', 'java', 'javascript'])
