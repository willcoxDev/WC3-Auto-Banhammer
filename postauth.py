import requests
import mechanicalsoup
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import sys
import time


url_home = 'https://4v4.vampirism.eu/'
url_ban = 'https://4v4.vampirism.eu/bancp/bancp.php'
USERNAME = 'XXXXXX'
PASSWORD = 'XXXXXXXXXXXX'
banned_list = 'C:\\XXXXXX\\banlist.txt'



def find_name():
    bad_name = ""
    response = requests.get(url_home, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    c = BeautifulSoup(response.content)
    for word in c.text.split():
        if 'iq55' in word.lower():
            bad_name = word
            print("\n\nBanned player found: %s" % word)
    if bad_name == "":
        print("\n\nNo banned players found")
    return bad_name


def add_to_list(initial_ban_name):
    add = False
    if initial_ban_name not in open(banned_list).read():
        with open(banned_list, 'a') as file:
            file.write('%s\n' % initial_ban_name)
            print("Banned player name ADDED to the text file list")
            add = True
            file.close()
            return add
    else:
        print("Banned player name is already on the text file list")
        return add




def sleep_bot():
    print("\nbot is sleepy, waiting 10 seconds")
    for x in range(10,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("%s seconds remaining" %x)
        sys.stdout.flush()
        time.sleep(1)


def post(initial_ban_name):
    requests.post(url_ban, auth=HTTPBasicAuth(USERNAME, PASSWORD), data=payload)
    print("Player: %s has been successfully banned" % initial_ban_name)


while True:
    ban_on_website = False
    initial_ban_name = find_name()
    if initial_ban_name != "":
        ban_on_website = add_to_list(initial_ban_name)
    payload = {
        'banneduser': initial_ban_name,
        'reason': 'other',
        'reason1': 'Ban Avoidance',
        'server': 'allrealms',
        'length': '1'
    }
    if ban_on_website:
        post(initial_ban_name)
    sleep_bot()
