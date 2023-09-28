# -*- coding: utf-8 -*-
import datetime
import logging
import os
import time

from singleton import SingletonClass


class number(metaclass=SingletonClass):
    # _num = None
    def __init__(self, num):
        print("here")
        self._num = num

    def get_num(self):
        return self._num

    def set_num(self, value):
        if isinstance(value, int):
            self._num = value

class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# python 3 style
class MyLogger(object, metaclass=SingletonType):
    # __metaclass__ = SingletonType   # python 2 Style
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s\t[%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        now = datetime.datetime.now()
        dirname = "./log"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        # Generate new instance

    def get_logger(self) -> logging:
        return self._logger

# a simple usecase
if __name__ == "__main__":
    logger = MyLogger.__call__().get_logger()
    logger.info("Hello, Logger")
    logger.debug("bug occured")
