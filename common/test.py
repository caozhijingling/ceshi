'''
1.输入admin，输入19901201SsSzy,点击登录
2.输入admin，输入     ，点击登录
3.输入admin，输入19901201Szy,点击保持登录。点击登录
4.点击忘记密码
'''
from selenium import webdriver
import unittest
from lian.test import Login_page,url


class Logincase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_page = Login_page(cls.driver)


    def setUp(self):
        self.driver.get(url)
        self.login_page.is_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_1(self):
        '''输入admin，输入19901201SsSzy,点击登录'''
        self.login_page.input_user("admin")
        self.login_page.input_pwd("19901201Szy")
        self.login_page.click_login()

        result = self.login_page.get_login_user()
        self.assertTrue(result == "admin")



    def test_2(self):
        '''入admin，输入     ，点击登录'''
        self.login_page.input_user("admin")
        self.login_page.input_pwd("")
        self.login_page.click_login()

        result = self.login_page.get_login_user()
        self.assertTrue(result == "")



    def test_3(self):
        '''输入admin，输入19901201Szy,点击保持登录。点击登录'''
        self.login_page.input_user("admin")
        self.login_page.input_pwd("19901201Szy")
        self.login_page.click_keep_login()
        self.login_page.click_login()

        result = self.login_page.get_login_user()
        self.assertTrue(result == "admin")


    def test_4(self):
        '''点击忘记密码'''
        self.login_page.click_forget_pwd()

        result = self.login_page.is_fresh_exit()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "--main__":
    unittest.main()
