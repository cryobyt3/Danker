from colored import fg, bg, attr
import requests
import time
import re


# setting cli colors variables
reset = attr('reset')
red = fg(1)
green = fg(2)
yellow = fg(3)
cyan = fg(6)

def Beg_Send(channel, token):

    # setting url, data and headers for post request
    url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
    data = {'content': 'pls beg'}
    headers = {
        'authorization': token
    }

    # posting request and setting the response to a variable 'r'
    r = requests.post(url, data, headers=headers)

    # checking if message was sent successfully
    if str(r).__contains__("200"):
        return True
    else:
        print(red + 'Skipping command' + reset + '')
        return False

def Beg_Check(channel, token):
    
    # send command
    s = Beg_Send(channel, token)

    # pre-define a tries variable
    tries = 10

    # check response
    if s:
        while True:
            try:
                # setting url, data and headers for get request
                url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
                headers = {
                    'authorization': token
                }

                # posting request and setting the response to a variable 'r'
                r = requests.get(url, headers=headers) 

                # converting the variable to json and grabbing the first split
                r = r.json()[0]

                # check if dank memer sent the message
                if str(r['author']['id']) == "270904126974590976":
                    # check if dank memer replied to your message
                    url = 'https://discord.com/api/v9/users/@me'

                    # getting userid
                    user_id = requests.get(url, headers=headers)
                    user_id = user_id.json()['id']

                    # check if the user_id matches the replied message
                    if str(r['mentions'][0]['id']) == str(user_id):
                        return True, r
                    else:
                        raise Exception()
                else:
                    raise Exception()
            except:
                # check if there are no more tries left
                if tries == 0:
                    # go back if no more tries left
                    print(red + 'Skipping command' + reset + '')
                    return False, False
                    break
                else:
                    # retry if there are tries left
                    tries -= 1
    else:
        print(red + 'Skipping command' + reset + '')
        return False, False

def Beg(channel, token):

    # checking if dank memer responded
    s, r = Beg_Check(channel, token)

    # pre-defining variable
    coins = 0

    if s == True:
        # grab the content from the response
        content = str(r['content'])

        # check if content is embeded
        if content == '':
            # set content to the embeded
            content = r['embeds'][0]['description']

        # remove ',' from content
        content = content.replace(',', '')
        # check if got coins
        if content.__contains__('⏣'):
            # split content at ⏣
            content1, content2 = content.split('⏣')
            # grab the coins
            coins += int(re.findall('\d+', content2)[0])

        # return coins earned
        return coins