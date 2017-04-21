"""
Quickie Media - Twitter (Arnold 2.0)
"""

from __future__ import print_function
import twitter
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz


def convert_time(datestring):
    timestamp = mktime_tz(parsedate_tz(datestring))
    s = str(datetime.fromtimestamp(timestamp))
    return s


def print_timeline(status):
    # modifies header length based on screen_name length
    dash = ""
    for i in range(0, len(status.user.screen_name)):
        dash = dash + "-"

    # print(status)
    print("\n--------------------------------------------------" + str(dash))
    print(status.user.screen_name, "| ", end="")
    print(convert_time(status.created_at), "| ", end="")
    print("Likes:", status.favorite_count, "| ", end="")
    print("Retweets:", status.retweet_count, "| ")
    print("--------------------------------------------------" + str(dash))
    print(status.text)
    print("--------------------------------------------------" + str(dash))


def get_timeline(api):
    data = api.GetHomeTimeline(count=3)
    for status in data:
        print_timeline(status)


if __name__ == "__main__":
    get_timeline()

