#!/usr/bin/env python

import json
import sys
from argparse import ArgumentParser
from random import randint
from requests import get, post
from requests.auth import HTTPBasicAuth

ACCOUNT_SID = ''
AUTH_TOKEN = ''
FROM_NUMBER = ''

auth = HTTPBasicAuth(ACCOUNT_SID, AUTH_TOKEN)

def get_giphy(search):
    # Note that is the giphy test API Key. If you use this a lot you should
    # request an API key from the giphy team.
    params = {
        'q': search,
        'api_key': 'dc6zaTOxFJmzC'
    }
    res = get('http://api.giphy.com/v1/gifs/search', params=params)

    if res.status_code != 200:
        return None

    results = json.loads(res.content)
    images = results['data']
    i = randint(0, len(images) - 1)

    return images[i]['images']['fixed_height']['url']

def spam(pn, body, image_url):
    print "Spamming {}".format(pn)
    payload = {
        'To' : pn,
        'From': FROM_NUMBER,
        'Body': body,
        'MediaUrl': image_url
    }
    post("https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(ACCOUNT_SID), auth=auth, data=payload)


def create_arg_parser():
    parser = ArgumentParser(description="Query Giphy and send an MMS")
    parser.add_argument('-q', dest='query', type=str)
    parser.add_argument('--body', dest='message', type=str, required=False)
    parser.add_argument('--to', dest='phone_numbers', type=str, nargs='+')
    return parser


if __name__ == "__main__":
    args = create_arg_parser().parse_args()
    if args.query is None or args.phone_numbers is None:
        sys.exit(1)

    gif = get_giphy(args.query)
    if gif is None:
        print "Could not find gif for query {}".format(args.query)
    else:
        print "Got {} from giphy".format(gif)
        message = args.query if args.message is None else args.message
        [spam(pn, args.message, gif) for pn in args.phone_numbers]
