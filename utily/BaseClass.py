import inspect

import pytest
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass


    def getlogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)  # __name__ will get the class name
        filehandler = logging.FileHandler("logging.log")  # for opening the file
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")  # in the format
        filehandler.setFormatter(formatter)  # add the logging format
        logger.addHandler(filehandler)  # adding the handler
        logger.setLevel(logging.INFO)  # set level -info,error, warning ,debug
        logger.debug("in the debuging mode")
        logger.info("display info")
        logger.warning("warning shown")
        logger.error("an critical error")
        logger.critical("critical issue")
        return  logger




