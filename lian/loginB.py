# 案列1
from selenium import webdriver
import unittest
from lian.loginA import login

class Denglu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_1(self):
        login(self.driver)

    if __name__ == "__main__":
        unittest.main()