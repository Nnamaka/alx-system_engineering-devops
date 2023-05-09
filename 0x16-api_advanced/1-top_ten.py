#!/usr/bin/python3
""" Prints first 10 hot post """


def top_ten(subreddit):
    """ returns top 10 post """

    api = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    res = requests.get(api, params=10)

    if res.status_code != 200:
        print('None')
        return

    for child in res.json().get('data').get('children'):
        print(child.get('data').get('title'))
