from config_parser import Configurator
from colored import fg, bg, attr
from token_finder import Tokens
from discord_hook import RQ
from os import path
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('option')
parser.add_argument('token')
parser.add_argument('private')
parser.add_argument('config')
args = parser.parse_args()

try:
    if int(args.token) == 0:
        pass
    else:
        Configurator.update_value('RSA', 'token', args.token)
    if int(args.private) == 0:
        pass
    else:
        Configurator.update_value('RSA', 'private', args.private)
except:
    pass

Configurator.path(args.config)

if int(args.option) == 0:
    tokens = Tokens.print_tokens()
    for t in tokens:
        print(t)
    token = int(input("\nWhich token do you wish to use?: "))
    token = tokens[token]
    token = token.split(': ')[1]
    Tokens.generate_key(Configurator.get_value("RSA", 'public'), Configurator.get_value("RSA", 'private'))
    token = Tokens.encrypt(token, Configurator.get_value("RSA", 'public'))
    with open("token", "wb") as f:
        f.write(token)
elif int(args.option) == 1:
    RQ.Start()
elif int(args.option) == 2:
    RQ.SellAll()
elif int(args.option) == 3:
    RQ.Snake_Eyes()