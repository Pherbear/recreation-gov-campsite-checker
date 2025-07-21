# -*- coding: utf-8 -*-
import json
import random
import sys
import time
from hashlib import md5
from os import isatty
import requests

from enums.emoji import Emoji

MAX_TWEET_LENGTH = 279
DELAY_FILE_TEMPLATE = "next_{}.txt"
DELAY_TIME = 1800

def send_notification(notif):
    print(notif)

    token = 'your_app_token_here'
    user = 'your_user_key_here'

    data = {
        'token': token,
        'user': user,
        'message': notif
    }

    response = requests.post('https://api.pushover.net/1/messages.json', data=data)
    print(f"Status: {response.status_code}, Response: {response.text}")

    print('notification has been sent!')

def main(stdin):
    first_line = next(stdin)

    if "Something went wrong" in first_line:
        send_notification("I'm broken! Please help :'(")
        sys.exit()

    available_site_strings = generate_availability_strings(stdin)

    if available_site_strings:
        tweet = generate_notification_str(available_site_strings, first_line)
        send_notification(tweet)
        sys.exit(0)
    else:
        print("No campsites available, not tweeting 😞")
        sys.exit(1)


def generate_notification_str(available_site_strings, first_line):
    tweet = first_line.rstrip()
    tweet += " 🏕🏕🏕\n"
    tweet += "\n".join(available_site_strings)
    tweet += "\n" + "🏕" * random.randint(5, 20)  # To avoid duplicate tweets.
    return tweet


def generate_availability_strings(stdin):
    available_site_strings = []
    for line in stdin:
        line = line.strip()
        if Emoji.SUCCESS.value in line:
            park_name_and_id = " ".join(line.split(":")[0].split(" ")[1:])
            num_available = line.split(":")[1][1].split(" ")[0]
            s = "{} site(s) available in {}".format(
                num_available, park_name_and_id
            )
            available_site_strings.append(s)
    return available_site_strings


if __name__ == "__main__":
    main(sys.stdin)
