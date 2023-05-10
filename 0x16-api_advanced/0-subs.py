#!/usr/bin/python3
""" Get number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    header = {'User-Agent': 'shell magic'}

    api = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)

    res = requests.get(api, headers=header)

    if res.status_code != 200:
        return (0)

    subscribers = res.json().get('data').get('subscribers')

    return subscribers
