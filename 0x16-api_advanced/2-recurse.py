#!/usr/bin/python3
""" recursively query reddit api """
import requests

def recurse(subreddit, hot_list=[],count=0, after=None):
    """ query reddit api and return  a list of hot aticles titles """
    
    header = {'User-Agent': 'How often'}
    values = {'limit':3, 'after':after, 'count':count}
    api = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    res = requests.get(api, headers=header, params=values, allow_redirects=False)
    
    if res.status_code == 200:
        count += res.json().get("data").get("dist")
        after = res.json().get("data").get("after")

        for item in res.json().get("data").get("children"):
            hot_list.append(item.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, count, after)
        else:
            return hot_list if hot_list else None
    
    return hot_list if hot_list else None
