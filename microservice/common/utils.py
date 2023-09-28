import pandas
import git
import random
import string
import configparser
import os
from functools import wraps

def save_data_frame_to_csv(data_frame:pandas.DataFrame, filename:str) ->None:
    data_frame.to_csv(filename)

def get_git_root(path:str) -> str:
    """get parrent git path

    Args:
        path (str)

    Returns:
        str: parrent git path
    """
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root

def get_random_letter(length) -> str:
    # choose from all ascii letter
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

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

def show_fucntion_name(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper