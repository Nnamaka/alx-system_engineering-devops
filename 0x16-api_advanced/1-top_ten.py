#!/usr/bin/python3
""" Prints first 10 hot post """
import requests


def top_ten(subreddit):
    """ returns top 10 post """

    api = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-Agent': 'priceless stuff'}

    res = requests.get(api, headers=header, params={
                       'limit': 10}, allow_redirects=False)

    if res.status_code != 200:
        print('None')
        return

    for child in res.json().get('data').get('children'):
        print(child.get('data').get('title'))
