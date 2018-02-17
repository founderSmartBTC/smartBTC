# --------------- Dependencies ------------------------
# The bellow line should be used in dependencies textbox
# pip install requests

# --------------- Contract Body ---------------------
import requests


def contract():
    desired_nr_of_followers = 1000
    twitter_screen_name = "smartBtcIO"

    twitter_response = requests.get("https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names={}".
                                    format(twitter_screen_name)).json();
    count = twitter_response[0]['followers_count']
    print 'current followers: ' + str(count)

    if count >= desired_nr_of_followers:
        print 'Contract done.'
        return True
    else:
        print 'Contract NOT done! Still need an extra: {} followers'.format(desired_nr_of_followers-count)
        return False