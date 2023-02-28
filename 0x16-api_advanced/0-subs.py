#!/usr/bin/python3
""" fetch the nuber of subscribers of a subreddit from reddit """
import json
import requests


def number_of_subscribers(subreddit):
    """ shows the number of subscribers a subredit """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    res = requests.get(url)
    d = json.loads(res.text)
    subs = d['data']['children'][1]['data']['subreddit_subscribers']
    return int(subs)
