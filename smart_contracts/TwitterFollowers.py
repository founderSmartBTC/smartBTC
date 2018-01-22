# --------------- Dependencies ------------------------
# The bellow line should be used in dependencies textbox
# pip install requests

# --------------- Contract Body ---------------------
import time
import requests


def contract():
    nr_of_followers = 1000
    print 'Inside Contract'
    print 'Current time: ' + time.strftime("%Y-%m-%d %H:%M")
    twitter_response = requests.get("https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=smartBtcIO").json();
    count = twitter_response[0]['followers_count']
    print 'current followers: ' + str(count)

    if count > nr_of_followers:
        print 'Contract done.'
        return True
    else:
        print 'Contract NOT done! Still need an extra: {} followers'.format(nr_of_followers-count)
        return False

#contract()