import os
import sys
import configparser

def read_config(path:str) -> dict:
    """read config file

    Args:
        path (str): path of config file

    Raises:
        Exception: if file is not exists

    Returns:
        dict: config base on key and value
    """
    if not os.path.exists(path):
        raise Exception("Can not read {}".format(path))
    config = configparser.ConfigParser()
    config.optionxform=str
    config.read(path)
    return config

