from discord.token_finder import *
from discord.options import *
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument('option')
args = parser.parse_args()

if int(args.option) == 0:
    Run_Setup()
elif int(args.option) == 1:
    Run_Once()
elif int(args.option) == 2:
    Overnight()
elif int(args.option) == 3:
    SellAll()