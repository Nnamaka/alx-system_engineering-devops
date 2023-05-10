#!/usr/bin/python3
""" Get number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    if type(subreddit) != str:
        return (0)

    api = 'http://www.reddit.com/r/{}/about'.format(subreddit)

    res = requests.get(api)

    if res.status_code != 200:
        return (0)

    subsribers = res.json().get('data').get('subscribers')

    return subscribers
