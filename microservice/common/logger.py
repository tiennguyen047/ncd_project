# -*- coding: utf-8 -*-
import datetime
import logging
import os
# import time
import sys
sys.path.insert(0, "/home/ziuteng/ncd_proj/ncd_project/microservice/")
from common.constants import LOG
from common.singleton import SingletonType

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

def embrace(func):
    logger = get_logger()
    def wrapper(*args, **kwargs):
        logger.info("Call function {}".format(func.__name__), stack_info=False)
        return func(*args, **kwargs)
    return wrapper