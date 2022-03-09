import inspect
import logging

import pytest
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("setup")
class Base_class:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log', encoding="UTF-8")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def action_move_to_element(self, locator):
        action = ActionChains(self.driver)
        return action.move_to_element(locator)
