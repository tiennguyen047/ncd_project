import configparser

class BaseConfig(configparser.ConfigParser):
    def __init__(self, *arg):
        config = configparser.ConfigParser()
        config.read(arg[0])

# class Config_pas
