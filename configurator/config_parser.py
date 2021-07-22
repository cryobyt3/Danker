import configparser
import platform
import json
import os


# initializing a ConfigParser
config = configparser.ConfigParser()
# reading the config file
config.read('configs/_.cfg')

# getting the config_path from the config and setting it as a variable con_path
con_path = config.get('PATHS', 'config_path')

# reading new config file
config = configparser.ConfigParser()
config.read(con_path)

# defining a get_value function with section and value
def get_value(section, value):
    # returning the value of the respecting section
    return config.get(str(section), str(value))

# defining an update_value function with section, value and new_value
def update_value(section, value, new_value):
    # setting the value in the respective section to the new_value
    config.set(str(section), str(value), str(new_value))
    # oppening the config file
    with open(con_path, 'w') as cf:
        # writing new changes
        config.write(cf)

# defining a get_options function
def get_options():
    # getting values of search options and setting them accordingly
    search0 = config.get('SEARCH', 'search0')
    search1 = config.get('SEARCH', 'search1')
    search2 = config.get('SEARCH', 'search2')
    search3 = config.get('SEARCH', 'search3')
    search4 = config.get('SEARCH', 'search4')
    search5 = config.get('SEARCH', 'search5')
    search6 = config.get('SEARCH', 'search6')
    search7 = config.get('SEARCH', 'search7')
    search8 = config.get('SEARCH', 'search8')
    search9 = config.get('SEARCH', 'search9')
    search10 = config.get('SEARCH', 'search10')
    search11 = config.get('SEARCH', 'search11')
    search12 = config.get('SEARCH', 'search12')
    search13 = config.get('SEARCH', 'search13')
    search14 = config.get('SEARCH', 'search14')
    search15 = config.get('SEARCH', 'search15')
    search16 = config.get('SEARCH', 'search16')
    search17 = config.get('SEARCH', 'search17')
    search18 = config.get('SEARCH', 'search18')
    search19 = config.get('SEARCH', 'search19')
    search20 = config.get('SEARCH', 'search20')
    search21 = config.get('SEARCH', 'search21')
    search22 = config.get('SEARCH', 'search22')
    search23 = config.get('SEARCH', 'search23')
    search24 = config.get('SEARCH', 'search24')
    search25 = config.get('SEARCH', 'search25')
    search26 = config.get('SEARCH', 'search26')
    search27 = config.get('SEARCH', 'search27')
    search28 = config.get('SEARCH', 'search28')
    search29 = config.get('SEARCH', 'search29')
    search30 = config.get('SEARCH', 'search30')
    search31 = config.get('SEARCH', 'search31')
    search32 = config.get('SEARCH', 'search32')

    # returning search options
    return search0, search1, search2, search3, search4, search5, search6, search7, search8, search9, search10, search11, search12, search13, search14, search15, search16, search17, search18, search19, search20, search21, search22, search23, search24, search25, search26, search27, search28, search29, search30, search31, search32