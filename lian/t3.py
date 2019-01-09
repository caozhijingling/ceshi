# def bbc(a, b):
#     c = a * b
#     return c
#
# if __name__ == "__main__":
#     t = bbc(4, 5)
#     print(t)


from selenium import webdriver
import time
import unittest

class Youxiang(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://exmail.qq.com/")
        time.sleep(2)
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
    def sucess(self):
        try:
            t = self.driver.find_element_by_css_selector("#folder_1").text
            print(t)
            return t
        except:
            return ""


    def test_1(self):
        # 正确的账户和密码
        self.driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        self.driver.find_element_by_class_name("js_show_pwd_panel").click()
        self.driver.find_element_by_id("inputuin").send_keys("yangqin@beidouapp.com")
        self.driver.find_element_by_id("pp").send_keys("19901201Szy")
        self.driver.find_element_by_id("auto_login_in_five_days_pwd").click()
        self.driver.find_element_by_id("btlogin").click()
        time.sleep(1)

        t = self.sucess()
        self.assertTrue(t=="收件箱")


    def test_2(self):
        # 错误的账户和密码
        self.driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("js_show_pwd_panel").click()
        time.sleep(1)
        self.driver.find_element_by_id("inputuin").send_keys("yangqin@beidouapp.com")
        self.driver.find_element_by_id("pp").send_keys("19901201")
        self.driver.find_element_by_id("auto_login_in_five_days_pwd").click()
        self.driver.find_element_by_id("btlogin").click()
        time.sleep(1)

        t = self.sucess()
        print("登录失败 结果是%s" %t)
        self.assertTrue(t == "")









if __name__ == "__main__":
    unittest.main()


