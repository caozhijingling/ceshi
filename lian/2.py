# 2用unittest实现
# from selenium import webdriver
# import time
# import unittest
#
# class DengLu(unittest.TestCase):
#     def test_1(self):
#         driver = webdriver.Firefox()
#         driver.get("http://127.0.0.1/zentao/user-login.html")
#         time.sleep(2)
#
#         driver.find_element_by_id("account").send_keys("admin")
#         driver.find_element_by_name("password").send_keys("19901201Szy")
#         driver.find_element_by_id("keepLoginon").click()
#         driver.find_element_by_id("submit").click()
#         time.sleep(2)
#
#         t = driver.find_element_by_css_selector(".user-name").text
#         print(t)
#         self.assertTrue("t==admin")





from selenium import webdriver
import time
import unittest

class Youxiang(unittest.TestCase):

    def test_2(self):
        driver = webdriver.Firefox()
        driver.get("https://exmail.qq.com/")
        time.sleep(2)

        driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        time.sleep(2)

        driver.find_element_by_class_name("js_show_pwd_panel").click()
        time.sleep(2)

        driver.find_element_by_id("inputuin").send_keys("yangqin@beidouapp.com")
        driver.find_element_by_id("pp").send_keys("19901201Szy")
        driver.find_element_by_id("btlogin").click()
        time.sleep(2)

        t = driver.find_element_by_css_selector("#folder_1").text
        print(t)

        self.assertTrue("t==收件箱")

if __name__ == "__main__":
    unittest.main()







