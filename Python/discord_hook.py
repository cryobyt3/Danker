from config_parser import Configurator
from fast_requests import Sender
from colored import fg, bg, attr
from token_finder import Tokens
import threading
import requests
import random
import time


class RQ:

    def __init__():
        pass

    def Get():
        channel = Configurator.get_value('OPTIONS', 'channel')
        token = open(str(Configurator.get_value('RSA', 'token')), 'rb').read()
        priv_path = Configurator.get_value('RSA', 'PRIVATE')
        token = Tokens.decrypt(token, priv_path)
        token = token.decode()
        channel = Configurator.get_value('OPTIONS', 'channel')
        c_items = Configurator.get_value('OPTIONS', 'check-items')
        delay = Configurator.get_value('OPTIONS', 'wait-between-options')
        cycle_time = Configurator.get_value('OPTIONS', 'wait-between-cycles')
        search_wait = Configurator.get_value('OPTIONS', 'wait-for-search')
        return channel, token, delay, cycle_time, search_wait, c_items

    @staticmethod
    def Check_Enabled(option):
        commands = ['beg', 'search', 'fish', 'hunt', 'dig', 'pm', 'loop']
        for c in commands:
            if c == option:
                if Configurator.get_value('OPTIONS', c) == "True": return True
                else: return False

    @staticmethod
    def Start():
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)
        channel, token, delay, cycle_time, search_wait, c_items = RQ.Get()
        if c_items == 'True':
            items = RQ.Get_Items()
        else:
            items = ['fishing', 'rifle', 'shovel', 'laptop']
        coins = 0
        timer = 18000
        cycles = 0

        if RQ.Check_Enabled('loop'):
            while timer > 0:
                time.sleep(cycles * 60)
                cycles = int(random.randint(20, 30))
                tcycles = cycles

                while cycles != 0:
                    cycles -= 1
                    final_time = 0

                    # pls beg
                    if RQ.Check_Enabled('beg'):
                        Sender.Send('pls beg', channel, token)
                        tcoins, tbank = Sender.Get_Coins(channel, token)
                        coins += tcoins
                        print("Coins: " + yellow + str(tcoins) + reset + "")
                        if tbank:
                            Sender.Use_Banknote(channel, token)
                        twait = int(random.randint(1, 5))
                        final_time += twait
                        time.sleep(twait)

                    # pls search
                    if RQ.Check_Enabled('search'):
                        Sender.Send('pls search', channel, token)
                        time.sleep(int(search_wait))
                        option = Sender.Get_Search(channel, token)
                        Sender.SilentSend(str(option), channel, token)
                        tcoins, tbank = Sender.Get_Coins(channel, token)
                        coins += tcoins
                        print("Coins: " + yellow + str(tcoins) + reset + "")
                        if tbank:
                            Sender.Use_Banknote(channel, token)
                        twait = int(random.randint(1, 5))
                        final_time += twait
                        time.sleep(twait)

                    # pls fish
                    if RQ.Check_Enabled('fish'):
                        if items.__contains__('fishing'):
                            Sender.Send('pls fish', channel, token)
                            tcoins, tbank = Sender.Get_Coins(channel, token)
                            coins += tcoins
                            print("Coins: " + yellow + str(tcoins) + reset + "")
                            if tbank:
                                Sender.Use_Banknote(channel, token)
                            twait = int(random.randint(1, 5))
                            final_time += twait
                            time.sleep(twait)
                        else:
                            print(red + '\nNo Fishing Rod. Skipping...' + reset + "")

                    # pls hunt
                    if RQ.Check_Enabled('hunt'):
                        if items.__contains__('rifle'):
                            Sender.Send('pls hunt', channel, token)
                            tcoins, tbank = Sender.Get_Coins(channel, token)
                            coins += tcoins
                            print("Coins: " + yellow + str(tcoins) + reset + "")
                            if tbank:
                                Sender.Use_Banknote(channel, token)
                            twait = int(random.randint(1, 5))
                            final_time += twait
                            time.sleep(twait)
                        else:
                            print(red + '\nNo Hunting Rifle. Skipping...' + reset + "")

                    # pls dig
                    if RQ.Check_Enabled('dig'):
                        if items.__contains__('shovel'):
                            Sender.Send('pls dig', channel, token)
                            tcoins, tbank = Sender.Get_Coins(channel, token)
                            coins += tcoins
                            print("Coins: " + yellow + str(tcoins) + reset + "")
                            if tbank:
                                Sender.Use_Banknote(channel, token)
                            twait = int(random.randint(1, 5))
                            final_time += twait
                            time.sleep(twait)
                        else:
                            print(red + '\nNo Shovel. Skipping...' + reset + "")

                    # pls pm
                    if RQ.Check_Enabled('pm'):
                        if items.__contains__('laptop'):    
                            Sender.Send('pls pm', channel, token)
                            time.sleep(.1)
                            Sender.SilentSend('r', channel, token)
                            tcoins, tbank = Sender.Get_Coins(channel, token)
                            coins += tcoins
                            print("Coins: " + yellow + str(tcoins) + reset + "")
                            if tbank:
                                Sender.Use_Banknote(channel, token)
                            twait = int(random.randint(1, 5))
                            final_time += twait
                            time.sleep(twait)
                        else:
                            print(red + '\nNo Laptop. Skipping...' + reset + "")

                    print("\nCycles left: " + cyan + str(cycles) + reset + "")
                    print("Repeating cylce in " + cyan + str(60 - final_time) + reset + " seconds.\n")
                    print("Total coins from all cycles" + reset + ": " + yellow + str(coins) + reset + "")
                    
                    time.sleep(60 - final_time)
                    
                print(red + 'Waiting to bypass Dank Memer auto ban.' + reset + "")
                t = tcycles * 60
                while t != 0:
                    print("Starting next cycles in: " + str(t))
                    time.sleep(1)
                    t -= 1
                timer -= tcycles * 60
                
            RQ.Start()

    @staticmethod
    def SellAll():
        channel, token, delay, cycle_time, search_wait, c_items = RQ.Get()
        sell_items = ['ant', 'boar', 'bread', 'cookie', 'deer', 'duck', 'exoticfish', 'garbage', 'jellyfish', 'junk', 'ladybug', 'rabbit', 'rarefish', 'seaweed', 'skunk', 'sand', 'stickbug', 'trash', 'worm', 'legendaryfish']

        for i in sell_items:
            Sender.Send('pls shop ' + str(i), channel, token)
            if Sender.Check_Item(channel, token):
                Sender.Send("pls sell " + str(i) + " all", channel, token)
            time.sleep(3)

    @staticmethod
    def Snake_Eyes():
        reset = attr('reset')
        red = fg(1)
        green = fg(2)
        yellow = fg(3)
        cyan = fg(6)
        channel, token, delay, cycle_time, search_wait, c_items = RQ.Get()
        wallet = None
        bank = None
        cycle = 0

        while True:
            if wallet == None and bank == None:
                Sender.SilentSend('pls bal', channel, token)
                wallet, bank = Sender.Get_Balance(channel, token)
            
            twallet = wallet
            wallet, bank = Sender.Get_Bet(channel, token, wallet, bank)
            if wallet < twallet:
                print('\nLost: ' + red + str(twallet - wallet) + reset + "")
            elif wallet > twallet:
                print('\nGained: ' + green + str(wallet - twallet) + reset + "")
            print('Finished cycle: ' + cyan + str(cycle) + reset + "")
            print('Repeating in ' + cyan + '7' + reset + ' seconds')
            time.sleep(7)
            cycle += 1
    
    @staticmethod
    def Get_Items():
        channel, token, delay, cycle_time, search_wait, c_items = RQ.Get()

        check_items = ['fishing', 'rifle', 'shovel', 'laptop']
        items = []

        for i in check_items:
            Sender.Send('pls shop ' + str(i), channel, token)
            if Sender.Check_Item(channel, token):
                items.append(i)
            time.sleep(3)

        return items