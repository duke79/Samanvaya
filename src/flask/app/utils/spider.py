import os

from selenium import webdriver


class Spider():
    def __init__(self):
        dir_utils = os.path.dirname(os.path.realpath(__file__))
        path_chromedriver = os.path.join(dir_utils, "chromedriver.exe")
        self._driver = webdriver.Chrome(path_chromedriver)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver().close()

    def driver(self):
        return self._driver
