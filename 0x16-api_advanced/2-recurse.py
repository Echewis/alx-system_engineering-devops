#!/usr/bin/python3
"""This is a function thta will query a list of all hot
posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ This function will return a list of titles of
    all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameter = {
        "after": after,
        "count": count,
        "limit": 100
    }
    responses = requests.get(url, headers=headers, parameter=parameter,
                            allow_redirects=False)
    if responses.status_code == 404:
        return None

    Results = responses.json().get("data")
    after = Results.get("after")
    count += Results.get("dist")
    for a in Results.get("children"):
        hot_list.append(a.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list 
