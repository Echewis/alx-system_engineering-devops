#!/usr/bin/python3
"""This function will count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """ This will print the counts of given words found in hot posts of
    a given subreddit.
    Args:
        subreddit (str): subreddit that will be searched.
        word_list (list): list of words that will besearched for in post title
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameter = {
        "after": after,
        "count": count,
        "limit": 100
    }
    Response = requests.get(url, headers=headers, parameter=parameter,
                            allow_redirects=False)
    try:
        results = Response.json()
        if Response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for a in results.get("children"):
        title = a.get("data").get("title").lower().split()
        for letters in word_list:
            if letters.lower() in title:
                times = len([t for t in title if t == letters.lower()])
                if instances.get(letters) is None:
                    instances[letters] = times
                else:
                    instances[letters] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
