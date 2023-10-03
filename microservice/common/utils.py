import pandas
import git
import random
import string
import configparser
import os
import xml.etree.ElementTree as ET

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

def read_xml(path):
    with open(path, "r") as file:
        xml_data = file.read()
    root = ET.fromstring(xml_data)
    res = [(elem.tag, elem.text) for elem in root.iter()]
    sessionId=list(filter(lambda element : "sessionId" in element[0], res))[0][1]
    baseSequenceId=list(filter(lambda element : "baseSequenceId" in element[0], res))[0][1]



if __name__ == "__main__":
    read_xml("/home/ziuteng/ncd_proj/ncd_project/microservice/common/res.xml")