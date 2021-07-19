import configparser
import platform
import os


con_path = r'configs/config.ini'

class Configurator:

    def __init__(self):
        pass
    
    @staticmethod
    def path(p):
        con_path = r'configs/' + p

    def get_value(section, value):
        config = configparser.ConfigParser()
        config.read(con_path)
        return config.get(str(section), str(value))

    def update_value(section, value, new_value):
        config = configparser.ConfigParser()
        config.read(con_path)
        config.set(str(section), str(value), str(new_value))
        with open(con_path, 'w') as cf:
            config.write(cf)