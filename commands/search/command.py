from configurator.config_parser import get_options
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

def Search_Send(message, channel, token):

    # setting url, data and headers for post request
    url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
    data = {'content': str(message)}
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

def Search_Check(message, channel, token):
    
    # send command
    s = Search_Send(message, channel, token)

    # pre-define a tries variable
    tries = 10

    # check response
    if s:
        while True:
            try:
                # setting url, data and headers for post request
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

def Search(channel, token):

    # getting search options
    search0, search1, search2, search3, search4, search5, search6, search7, search8, search9, search10, search11, search12, search13, search14, search15, search16, search17, search18, search19, search20, search21, search22, search23, search24, search25, search26, search27, search28, search29, search30, search31, search32 = get_options()

    # creating a checks variable with search options
    checks = [search0, search1, search2, search3, search4, search5, search6, search7, search8, search9, search10, search11, search12, search13, search14, search15, search16, search17, search18, search19, search20, search21, search22, search23, search24, search25, search26, search27, search28, search29, search30, search31, search32]

    # checking if dank memer responded
    s, r = Search_Check('pls search', channel, token)

    # pre-defining variable
    coins = 0

    if s:
        # get the 3 search options
        r = r['content'].split('\n')[2].split(',')
        r1 = str(r[0]).replace("`", "").replace(" ", "")
        r2 = str(r[1]).replace("`", "").replace(" ", "")
        r3 = str(r[2]).replace("`", "").replace(" ", "")

        # creating a list with the 3 search options
        r = [r1, r2, r3]

        # creating 3 empty variables
        p1, p2, p3 = 0, 0, 0

        # checking if the 3 options are in the checks list
        for indx, pick in enumerate(r):
            for i, option in enumerate(checks):
                if option == pick:
                    # assigning a value to the option
                    # depending on how far in the check list
                    # it was
                    if indx == 0:
                        temp = i
                        p1 = 33 - temp
                    elif indx == 1:
                        temp = i
                        p2 = 33 - temp
                    else:
                        temp = i
                        p3 = 33 - temp

        # checking if the first option is the best choice
        if p1 > p2 and p1 > p3:
            # assigning the choice to it
            choice = r[0]
        # checking if the second option is the best choice
        elif p2 > p1 and p2 > p3:
            # assigning the choice to it
            choice = r[1]
        # checking if the third option is the best choice
        elif p3 > p1 and p3 > p2:
            # assigning the choice to it
            choice = r[2]

        # send the choice and get response
        s, r = Search_Check(choice, channel, token)

        if s:
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