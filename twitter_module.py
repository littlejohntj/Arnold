"""
Quickie Media - Twitter (Arnold 2.0)
"""

from __future__ import print_function
import twitter
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz
import textwrap


def convert_time(datestring):
    timestamp = mktime_tz(parsedate_tz(datestring))
    s = str(datetime.fromtimestamp(timestamp))
    return s


def print_timeline(status):
    header = str(status.user.screen_name) + " | " + str(convert_time(status.created_at)) + " | " + "Likes: " \
           + str(status.favorite_count) + " | " + "Retweets: " + str(status.retweet_count) + " | "

    divider = ""
    for i in range(1, len(header)):
        divider = divider + "-"

    if len(status.text) > len(divider):
        status.text = textwrap.fill(status.text, len(divider))

    print("TWITTER")
    print(divider)
    print(header)
    print(divider)
    print(status.text)
    print(divider)
    print("\n")


def get_timeline(api):
    data = api.GetHomeTimeline(count=3)
    for status in data:
        print_timeline(status)


if __name__ == "__main__":
    get_timeline(api)
