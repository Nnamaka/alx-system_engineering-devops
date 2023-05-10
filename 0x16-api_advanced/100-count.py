#!/usr/bin/python3
""" Parses title and print sorted counts of given words """

import requests


def count_words(subreddit, word_list, titleDict={}, after=None):
    """ Recursive calls to the reddit api to find titles and sort them """

    header = {'User-Agent': 'How often'}
    values = {'limit': 3, 'after': after}
    api = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    if not titleDict:
        for word in word_list:
            if word.lower() not in titleDict:
                titleDict[word.lower()] = 0

    if after is None:
        values = list(titleDict.values())
        keys = list(titleDict.keys())

        values.sort(reverse=True)
        sortedValIdx = [i for i, x in sorted(
            enumerate(values), key=lambda x: x[1])]

        titleDict = {keys[i]: values[i] for i in sortedValIdx}

        for title in titleDict:
            if title[1] is not None:
                print('{}: {}'.format(title[0], title[1]))
        return None

    res = requests.get(api, headers=header, params=values,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    after = res.json().get("data").get("after")
    hot_articles = res.json().get("data").get("children")

    for article in hot_articles:
        keywords = [word.lower()
                    for word in article.get("data").get("title").split(" ")]

        for title in titleDict.keys():
            titleDict[title] += keywords.count(title)

    count_words(subreddit, word_list, titleDict, after)
