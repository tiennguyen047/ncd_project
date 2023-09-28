# -*- coding: utf-8 -*-
import datetime
import logging
import os
# import time
import sys
sys.path.insert(0, "/home/ziuteng/ncd_proj/ncd_project/microservice/")
from common.constants import LOG
# from singleton import SingletonClass

# class number(metaclass=SingletonClass):
#     # _num = None
#     def __init__(self, num):
#         print("here")
#         self._num = num

#     def get_num(self):
#         return self._num

#     def set_num(self, value):
#         if isinstance(value, int):
#             self._num = value

class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# python 3 style
class MyLogger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')
        # Generate new instance
        now = datetime.datetime.now()
        dirname = os.path.dirname(LOG)

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(LOG.format(now.strftime("%Y-%m-%d")))

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

    def get_logger(self) -> logging:
        return self._logger

def get_logger() -> logging:
    logger = MyLogger.__call__().get_logger()
    return logger


# a simple usecase for test, not using in code
# if __name__ == "__main__":
#     logger = get_logger()
#     logger.info("Hello, Logger")
#     logger.debug("bug occured")