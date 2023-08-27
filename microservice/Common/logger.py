# -*- coding: utf-8 -*-
import logging
import os
import datetime
from singleton import SingletonClass






class Logging(SingletonClass):
    def __init__(self) -> None:
        pass

class SingletonType(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls, *args, **kwargs)
        return cls._instances

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonClass):
    _logger = None

    def __init__(self) -> None:
        pass

    def __new__(cls, *args, **kwargs):
        if cls._logger is None:

            print("Logger is the first instances created")
            cls._logger = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("crumbs")
            cls._logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

            now = datetime.datetime.now()
            dirname = "./log"

            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fileHandler = logging.FileHandler(
                dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")

            streamHandler = logging.StreamHandler()

            fileHandler.setFormatter(formatter)
            streamHandler.setFormatter(formatter)

            cls._logger.addHandler(fileHandler)
            cls._logger.addHandler(streamHandler)

        return cls._logger
