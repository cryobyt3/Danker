from configurator.config_parser import get_value
from commands.search.command import *
from commands.fish.command import *
from commands.hunt.command import *
from commands.beg.command import *
from commands.dig.command import *
from discord.token_finder import *
from commands.pm.command import *
from colored import fg, bg, attr
from os import system, name
import configparser
import random
import time
import ast


# initializing a ConfigParser
config = configparser.ConfigParser()
# reading the config file
config.read('configs/_.cfg')

# getting the public and private path from the config and set them as variables
pubpath = config.get('PATHS', 'public_path')
privpath = config.get('PATHS', 'private_path')
tokenpath = config.get('PATHS', 'token_path')

if os.path.isfile(tokenpath):
    # getting token and channel and setting them in variables
    token = get_token()
    channel = get_channel()

# setting variables for cli colors
reset = attr('reset')
red = fg(1)
green = fg(2)
yellow = fg(3)
blue = fg(4)

# creating variables for wait times
check = get_value("OPTIONS", 'check-items')
beg_check = get_value('ENABLED', 'beg')
search_check = get_value('ENABLED', 'search')
fish_check = get_value('ENABLED', 'fish')
hunt_check = get_value('ENABLED', 'hunt')
dig_check = get_value('ENABLED', 'dig')
pm_check = get_value('ENABLED', 'pm')
wait_range1 = int(get_value('TIMINGS', 'wait-between-commands-range-1'))
wait_range2 = int(get_value('TIMINGS', 'wait-between-commands-range-2'))
cycles_range1 = int(get_value('TIMINGS', 'cycles-range1'))
cycles_range2 = int(get_value('TIMINGS', 'cycles-range2'))
cycle_time = int(get_value('TIMINGS', 'cycle-time'))
item_wait = 3

# defining a shop_item function with item
def shop_item(item):
    # setting url, data and headers for post request
    url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
    data = {'content': 'pls shop ' + item}
    headers = {
        'authorization': token
    }

    # posting request and setting the response to a variable 'r'
    r = requests.post(url, data, headers=headers)

    # checking if message was sent successfully
    if str(r).__contains__("200"):
        return True
    else:
        return False

# defining a shop_check function with item
def shop_check(item):

    # creating a tries variable
    tries = 10

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

            # checking if dank memer responded
            if str(r['author']['id']) == "270904126974590976":
                # checking if dank memer sent a shop embed
                if str(r).__contains__('SELL'):
                    # getting the title of the embed
                    title = r['embeds'][0]['title']
                    # checking if the title contains a number
                    if re.findall("\d+", title) != []:
                        return True
                        break
                    else:
                        return False
                        break

        except:
            # check if there are no more tries left
            if tries == 0:
                # go back if no more tries left
                return False
                break
            else:
                # retry if there are tries left
                tries -= 1

# defining a check_items function
def check_items():
    # creating a check_items list
    check_items = ['fishing', 'rifle', 'shovel', 'laptop']
    # creating an empty items list
    items = []

    # checking items
    for i in check_items:
        # sending pls shop (i)
        shop_item(i)
        # check if you have items
        if shop_check(i):
            # adding item to items list
            items.append(i)
        # waiting item_wait
        time.sleep(item_wait)

    # return items list
    return items
        
# defining a get_checks function
def get_checks():
    # getting values of checks from the config file
    check = get_value("OPTIONS", 'check-items')
    beg_check = get_value('ENABLED', 'beg')
    search_check = get_value('ENABLED', 'search')
    fish_check = get_value('ENABLED', 'fish')
    hunt_check = get_value('ENABLED', 'hunt')
    dig_check = get_value('ENABLED', 'dig')
    pm_check = get_value('ENABLED', 'pm')

    # returning the values
    return check, beg_check, search_check, fish_check, hunt_check, dig_check, pm_check
    
# defining a run_retup function
def Run_Setup():
    # if on windows clear the console
    if name == 'nt':
        _ = system('cls')
    
    # set the url and data variables
    url = 'https://api.auth.gg/v1/'
    data = {
        'type': 'redacted',
        'aid': 'redacted',
        'secret': 'redacted',
        'apikey': 'redacted'
    }

    # send post request
    r = requests.post(url, data=data)
    # grab cheat status
    status = r.json()['status']
    print('\n')
    print(blue + '                                   ██████╗  █████╗ ███╗  ██╗██╗  ██╗███████╗██████╗' + reset + '')
    print(blue + '                                   ██╔══██╗██╔══██╗████╗ ██║██║ ██╔╝██╔════╝██╔══██╗' + reset + '')
    print(blue + '                                   ██║  ██║███████║██╔██╗██║█████═╝ █████╗  ██████╔╝' + reset + '')
    print(blue + '                                   ██║  ██║██╔══██║██║╚████║██╔═██╗ ██╔══╝  ██╔══██╗' + reset + '')
    print(blue + '                                   ██████╔╝██║  ██║██║ ╚███║██║ ╚██╗███████╗██║  ██║' + reset + '')
    print(blue + '                                   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝' + reset + '')
    print('\n')
    print('                             ╔═══════════════════════════════════════════════════════════╗')
    if status == "Enabled":
        print('                             ║             Status is currently: ' + green + 'Undetected' + reset + '               ║')
    else:
        print('                             ║               Status is currently: ' + red + 'Detected' + reset + '               ║')
    print('                             ╚═══════════════════════════════════════════════════════════╝\n')
    # ask for user understanding
    if str(input('                        Do you understand that we do not guarantee that you will not get banned  \n                          and with that we do not take responsibility for your actions?\n                                                       (Y/N): ')) == "Y":
        # ask for user's token
        if str(input('\n                                           Do you have your discord token?\n                                                       (Y/N): ')) == "Y":
            token = str(input('\n                   Token: '))
            # generate an rsa key
            generate_key(pubpath, privpath)
            # encrypt the token with the public key
            token = encrypt(token, pubpath)
            # save the encrypted token to a file
            with open("token", "wb") as f:
                f.write(token)
            # exit
            exit(0)
        else:
            # if on windows clear the console
            if name == 'nt':
                _ = system('cls')
            print('\n')
            print(blue + '                                   ██████╗  █████╗ ███╗  ██╗██╗  ██╗███████╗██████╗' + reset + '')
            print(blue + '                                   ██╔══██╗██╔══██╗████╗ ██║██║ ██╔╝██╔════╝██╔══██╗' + reset + '')
            print(blue + '                                   ██║  ██║███████║██╔██╗██║█████═╝ █████╗  ██████╔╝' + reset + '')
            print(blue + '                                   ██║  ██║██╔══██║██║╚████║██╔═██╗ ██╔══╝  ██╔══██╗' + reset + '')
            print(blue + '                                   ██████╔╝██║  ██║██║ ╚███║██║ ╚██╗███████╗██║  ██║' + reset + '')
            print(blue + '                                   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝' + reset + '')
            print('\n')
            print('                             ╔═══════════════════════════════════════════════════════════╗')
            if status == 'Enabled':
                print('                             ║             Status is currently: ' + green + 'Undetected' + reset + '               ║')
            else:
                print('                             ║               Status is currently: ' + red + 'Detected' + reset + '               ║')
            print('                             ╚═══════════════════════════════════════════════════════════╝\n')
            # ask for permission to look for tokens
            permission = str(input('\n                                Do you allow us to automatically search for your token?\n                                                       (Y/N): '))
            if permission == "Y":
                # get tokens
                tokens = print_tokens()
                print('\n')
                # print tokens
                for idx, t in enumerate(tokens):
                    print('          ' + t)
                # ask for which token to be used
                token = tokens[int(input('\n          Choose your token: '))]
                # split the platform and get the token
                token = token.split(': ')[1]
                # generate an rsa key
                generate_key(pubpath, privpath)
                # encrypt the token with the public key
                token = encrypt(token, pubpath)
                # save the encrypted token to a file
                with open("token", "wb") as f:
                    f.write(token)
                # exit
                exit(0)
            elif permission == "N":
                exit()
    else:
        exit(0)

# defining a start function
def Run_Once():
    # getting check values from get_checks
    check, beg_check, search_check, fish_check, hunt_check, dig_check, pm_check = get_checks()
        
    # check if you have check-items enabled
    if check == 'True':
        # get owned items
        items = check_items()
        # check if pls fish is enabled
        if fish_check == 'True':
            # check if you have a fishing rod
            if items.__contains__('fishing'):
                # set pls fish to enabled
                fish_check = 'True'
            else:
                # set pls fish to disabled
                fish_check = False
        if hunt_check == 'True':
            # check if you have a rifle
            if items.__contains__('rifle'):
                # set pls hunt to enabled
                hunt_check = 'True'
            else:
                # set pls hunt to disabled
                hunt_check = False
        if dig_check == 'True':
            # check if you have a shovel
            if items.__contains__('shovel'):
                # set pls dig to enabled
                dig_check = 'True'
            else:
                # set pls dig to disabled
                dig_check = False
        if pm_check == 'True':
            # check if you have a laptop
            if items.__contains__('laptop'):
                # set pls pm to enabled
                pm_check = 'True'
            else:
                # set pls pm to disabled
                pm_check = False

    # checking if pls beg is enabled
    if beg_check == 'True':
        # running pls beg
        Beg(channel, token)
    # checking if pls search is enabled
    if search_check == 'True':
        # running pls search
        Search(channel, token)
    # checking if pls fish is enabled
    if fish_check == 'True':
        # running pls fish
        Fish(channel, token)
    # checking if pls hunt is enabled
    if hunt_check == 'True':
        # running pls hunt
        Hunt(channel, token)
    # checking if pls dig is enabled
    if dig_check == 'True':
        # running pls hunt
        Dig(channel, token)
    # checking if pls pm is enabled
    if pm_check == 'True':
        # running pls pm
        PM(channel, token)  

# defining an overnight farm function
def Overnight():
    # getting check values from get_checks
    check, beg_check, search_check, fish_check, hunt_check, dig_check, pm_check = get_checks()

    # check if you have check-items enabled
    if check == 'True':
        # get owned items
        items = check_items()
        # check if pls fish is enabled
        if fish_check == 'True':
            # check if you have a fishing rod
            if items.__contains__('fishing'):
                # set pls fish to enabled
                fish_check = 'True'
            else:
                # set pls fish to disabled
                fish_check = False
        if hunt_check == 'True':
            # check if you have a rifle
            if items.__contains__('rifle'):
                # set pls hunt to enabled
                hunt_check = 'True'
            else:
                # set pls hunt to disabled
                hunt_check = False
        if dig_check == 'True':
            # check if you have a shovel
            if items.__contains__('shovel'):
                # set pls dig to enabled
                dig_check = 'True'
            else:
                # set pls dig to disabled
                dig_check = False
        if pm_check == 'True':
            # check if you have a laptop
            if items.__contains__('laptop'):
                # set pls pm to enabled
                pm_check = 'True'
            else:
                # set pls pm to disabled
                pm_check = False

    while True:
        # generating a random integer from a range of
        # cycles_range1 to cycles_range 2 and storing
        # the value in cycles
        cycles = random.randint(cycles_range1, cycles_range2)
        # creating a variable with the value of cycles
        tcycles = cycles

        while cycles != 0:
            # subtract 1 from cycles
            cycles -= 1
            # set the total time to 0
            t_total = 0

            # checking if beg is enabled
            if beg_check == 'True':
                # execute commands and store coins received in coins
                coins = Beg(channel, token)
                print('\nExecuted: pls beg | Received: ' + yellow + str(coins) + reset + ' coins')
                # generating a random integer between the wait_ranges
                t = random.randint(wait_range1, wait_range2)
                # adding the integer to total time
                t_total += t
                # waiting for t
                time.sleep(t)  
            # checking if beg is enabled
            if search_check == 'True':
                # execute commands and store coins received in coins
                coins = Search(channel, token)
                print('\nExecuted: pls search | Received: ' + yellow + str(coins) + reset + ' coins')
                # generating a random integer between the wait_ranges
                t = random.randint(wait_range1, wait_range2)
                # adding the integer to total time
                t_total += t
                # waiting for t
                time.sleep(t)  
            # checking if beg is enabled
            if fish_check == 'True':
                # execute commands and store coins received in coins
                coins = Fish(channel, token)
                print('\nExecuted: pls fish | Received: ' + yellow + str(coins) + reset + ' coins')
                # generating a random integer between the wait_ranges
                t = random.randint(wait_range1, wait_range2)
                # adding the integer to total time
                t_total += t
                # waiting for t
                time.sleep(t)  
            # checking if beg is enabled
            if hunt_check == 'True':
                # execute commands and store coins received in coins
                coins = Hunt(channel, token)
                print('\nExecuted: pls hunt | Received: ' + yellow + str(coins) + reset + ' coins')
                # generating a random integer between the wait_ranges
                t = random.randint(wait_range1, wait_range2)
                # adding the integer to total time
                t_total += t
                # waiting for t
                time.sleep(t)   
            # checking if beg is enabled
            if dig_check == 'True':
                # execute commands and store coins received in coins
                coins = Dig(channel, token)
                print('\nExecuted: pls dig | Received: ' + yellow + str(coins) + reset + ' coins')
                # generating a random integer between the wait_ranges
                t = random.randint(wait_range1, wait_range2)
                # adding the integer to total time
                t_total += t
                # waiting for t
                time.sleep(t)    
            # checking if beg is enabled
            if pm_check == 'True':
                # execute commands and store coins received in coins
                coins = PM(channel, token)
                print('\nExecuted: pls pm | Received: ' + yellow + str(coins) + reset + ' coins')
                # generating a random integer between the wait_ranges
                t = random.randint(wait_range1, wait_range2)
                # adding the integer to total time
                t_total += t
                # waiting for t
                time.sleep(t)  

            # waiting for cycle_time - toatl time
            print("\nRepeating cylce in " + blue + str(cycle_time - t_total) + reset + " seconds.\n")
            time.sleep(cycle_time - t_total)   

        print(red + '\nWaiting to bypass Dank Memer auto ban.' + reset + "\n")
        # setting a t vraiable as total cycles * 60
        t = tcycles * 60
        # waiting for t before repeating cycles
        while t != 0:
            print("Starting next cycles in: " + blue + str(t) + reset + ' seconds')
            time.sleep(1)
            t -= 1

# defining a  sell_item function
def sell_item(item):
    # setting url, data and headers for post request
    url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
    data = {'content': 'pls sell ' + item + ' all'}
    headers = {
        'authorization': token
    }

    # posting request and setting the response to a variable 'r'
    r = requests.post(url, data, headers=headers)

# defining a SellAll function
def SellAll():
    # getting items to sell
    items = ast.literal_eval(str(get_value('OPTIONS', 'sell-items')))

    # checking items
    for i in items:
        # sending pls shop (i)
        shop_item(i)
        # check if you have items
        if shop_check(i):
            # sell item
            sell_item(i)
        # waiting item_wait
        time.sleep(item_wait)