#!/usr/bin/python3
""" fetch the nuber of subscribers of a subreddit from reddit """
from sys import argv
import json
from urllib import request


def number_of_subscribers(subreddit):
    """ shows the number of subscribers a subredit """
    param = argv[1]
    url = 'https://www.reddit.com/r/{}.json'.format(param)
    with request.urlopen(url) as res:
        if res.getcode() == 200:
            data = res.read()
            d = json.loads(data)
            subs = d['data']['children'][1]['data']['subreddit_subscribers']
            return int(subs)
