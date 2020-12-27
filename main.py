import requests
from datetime import datetime
import sendEmail
from sendEmail import sendMessage, emailContent
import time
from time import gmtime, strftime, localtime, timezone
from datetime import datetime
import pytz

country_time_zone = pytz.timezone('Turkey')

url = 'https://api.github.com/users/woosal1337/followers'
followerLst = []

f = open("login.0", "r")
username, token = f.readline().split(";")
f.close()

while True:

    getFollowers = requests.get(url, auth=(username, token)).json()

    if getFollowers != followerLst:
        for i in range(len(getFollowers)):
            if getFollowers[i]["id"] not in followerLst:
                action = ("User with ID of {0} has followed you!".format(getFollowers[i]["id"]))
                sendMessage(
                    "User with ID of {0} has UNFOLLOWED you!".format(getFollowers[i]["id"]),
                    "woosal1337@gmail.com",
                    "GitHub Follower!")
                print(action)

                f = open("logs.txt", "a")
                f.write(action + "\n")
                f.close()

        for j in range(len(followerLst)):
            if followerLst[j] not in getFollowers:
                action = ("User with ID of {0} has UNFOLLOWED you!".format(followerLst[j]))
                sendMessage(
                    "User with ID of {0} has UNFOLLOWED you!".format(followerLst[j]),
                    "woosal1337@gmail.com",
                    "GitHub Unfollower!")
                print(action)

                f = open("logs.txt", "a")
                f.write(action + "\n")
                f.close()

    followerLst = getFollowers

    time.sleep(60)
