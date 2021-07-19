from colored import fg, bg, attr
import requests
import time
import re


class Sender:

    def __init__():
        pass

    def Send(message, channel, token):
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)
        url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages'
        data = {'content': message}
        headers = {
            'authorization': token
        }

        try:
            r = requests.post(url, data, headers=headers)
            if str(r).__contains__("200"):
                print("\nCommand: " + message + "\nStatus: " + green + "sent successfully" + reset + "")
        except:
            print("\nCommand: " + message + "\nStatus: " + red + "retrying...\n" + reset + "")

    def SilentSend(message, channel, token):
        url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages'
        data = {'content': message}
        headers = {
            'authorization': token
        }

        try:
            r = requests.post(url, data, headers=headers)
        except:
            print('')

    @staticmethod
    def Check_Dank(channel, token):
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)

        tries = 10
        
        print('Status: ' + red + "attempting to grab Dank Memer response..." + reset + "")

        while True:
            try:
                url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
                headers = {
                    'authorization': token
                }

                r = requests.get(url, headers=headers) 
                r = r.json()[0]
                
                if str(r['author']['id']) == "270904126974590976":
                    url = 'https://discord.com/api/v9/users/@me'

                    user_id = requests.get(url, headers=headers)
                    user_id = user_id.json()['id']
                    if str(r['mentions'][0]['id']) == str(user_id):
                        print('Status: ' + green + 'response received' + reset + "")
                        return True, r, user_id
                    else:
                        raise Exception()
                else:
                    raise Exception()
            except:
                if tries == 0:
                    print('Status: ' + red + 'failed to grab response. Restarting loop...' + reset + "")
                    return False, '', ''
                    break
                else:
                    print('Status: ' + red + 'retrying... ' + str(tries) + ' attempts left' + reset + "")
                    tries -= 1

    def Get_Search(channel, token):
        checks = ["bus","coat","couch","dresser","fridge","grass","laundromat","mailbox","shoe","sink","vacuum","washer","attic","basement","bed","air","car","crawlspace","discord","dog","glovebox","mels room","uber","van","tree","dumpster","street","bushes","sewer","hospital","purse","bank","area51"]
        s, r, user_id = Sender.Check_Dank(channel, token)
        if s:
            r = r['content'].split('\n')[2].split(',')
            r1 = str(r[0]).replace("`", "")
            r1 = r1.replace(" ", "")
            r2 = str(r[1]).replace("`", "")
            r2 = r2.replace(" ", "")
            r3 = str(r[2]).replace("`", "")
            r3 = r3.replace(" ", "")

            r = [r1, r2, r3]
            p1, p2, p3 = 0, 0, 0

            for indx, pick in enumerate(r):
                for i, option in enumerate(checks):
                    if option == pick:
                        if indx == 0:
                            temp = i
                            p1 = 33 - temp
                        elif indx == 1:
                            temp = i
                            p2 = 33 - temp
                        else:
                            temp = i
                            p3 = 33 - temp

            if p1 > p2 and p1 > p3:
                choice = r[0]
            elif p2 > p1 and p2 > p3:
                choice = r[1]
            elif p3 > p1 and p3 > p2:
                choice = r[2]

            return choice

    def Get_Coins(channel, token):
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)
        try:
            s, r, user_id = Sender.Check_Dank(channel, token)
            coins = 0
            bank = False

            if s:
                content = str(r['content'])

                if content == '':
                    content = r['embeds'][0]['description']

                if content.__contains__("Bank Note"): bank = True
                content = content.replace(',', '')

                if content.__contains__('broken'):
                    print("Note: " + red + "Laptop Broke " + reset + "")
                else:
                    if content.__contains__('⏣'):

                        content1, content2 = content.split('⏣')
                        coins += int(re.findall('\d+', content2)[0])

                return coins, bank    
            else:
                return 0, False
        except:
            print(red + 'Error occured.' + red + '\nSkipping task.\n')

    def Use_Banknote(channel, token):
        Sender.Send('pls use bank', channel, token)
        time.sleep(1)
        Sender.Send('max', channel, token)

    @staticmethod
    def Check_Item(channel, token):

        while True:
            url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
            headers = {
                'authorization': token
            }

            r = requests.get(url, headers=headers) 
            r = r.json()[0]
            
            if str(r['author']['id']) == "270904126974590976":
                if str(r).__contains__('SELL'):
                    title = r['embeds'][0]['title']
                    if re.findall("\d+", title) != []:
                        return True
                        break
                    else:
                        return False
                        break

    @staticmethod
    def Get_Balance(channel, token):
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)
        while True:
            try:
                url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
                headers = {
                    'authorization': token
                }

                r = requests.get(url, headers=headers) 
                r = r.json()[0]
                
                if str(r['author']['id']) == "270904126974590976":
                    content = str(r['content'])
                    if content == '':
                        content = r['embeds'][0]['description']
                    content = content.replace(',', '')
                    content = content.split('/')[0]
                    if re.findall('\d+', content)[0] != 0 and re.findall('\d+', content)[1] != 0:
                        wallet = int(re.findall('\d+', content)[0])
                        bank = int(re.findall('\d+', content)[1])
                        if wallet + bank <= 4999:
                            print(red + 'You need a minimum of 5000 coins' + reset + "")
                            exit(0)

                        return wallet, bank
            except:
                print(red + 'Retrying...' + red)

    @staticmethod
    def Get_Bet(channel, token, wallet, bank):
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)

        if wallet + bank >= 2500000:
            if wallet >= 2500000:
                Sender.SilentSend('pls se max', channel, token)
            else:
                Sender.SilentSend('pls with all', channel, token)
                wallet += bank
                bank = 0
        elif wallet <= 5000:
            Sender.SilentSend('pls with all', channel, token)
            wallet += bank
            bank = 0

        if wallet + bank <= 2500000:
            Sender.SilentSend('pls se ' + str(int(wallet / 10)), channel, token)

        time.sleep(5)

        while True:
            try:
                url = 'https://discord.com/api/v9/channels/' + str(channel) + '/messages?limit=1'
                headers = {
                    'authorization': token
                }

                r = requests.get(url, headers=headers) 
                r = r.json()
                r = r[0]

                if str(r['author']['id']) == "270904126974590976":
                    r = r['embeds'][0]['description']
                    content = str(r)
                    if content.__contains__('1.8x'):
                        wallet += int(wallet / 10 * 1.8)
                    elif content.__contains__('10x'):
                        wallet += int(wallet / 10 * 10)
                    else:
                        wallet -= int(wallet / 10)
                    
                    return wallet, bank
                    break
                else:
                    pass
            except:
                print(red + 'Retrying...' + reset + "")
