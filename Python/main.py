from discord.token_finder import *
from discord.options import *
import argparse
import time


# create an argument parser
parser = argparse.ArgumentParser()
# add an option argument
parser.add_argument('option')
# get arguments
args = parser.parse_args()

# check if the argument is equal to zero
if int(args.option) == 0:
    # run setup
    Run_Setup()
# check if the argument is equal to one
elif int(args.option) == 1:
    # run once
    Run_Once()
# check if the argument is equal to two
elif int(args.option) == 2:
    # run overnight
    Overnight()
# check if the argument is equal to three
elif int(args.option) == 3:
    # sell all items
    SellAll()