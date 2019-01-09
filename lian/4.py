# from lianxi import t3
# d = t3.bbc(4, 6)
# print(d)



from selenium import webdriver
import time
# import unittest
#
# class Chandao(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("http://127.0.0.1/zentao/user-login.html")
#         time.sleep(1)
#
#
#     def tearDown(self):
#         self.alert()
#         self.driver.quit()
#
#
#
#     def sucess(self):
#         try:
#             t = self.driver.find_element_by_css_selector(".user-name").text
#             print(t)
#             return t
#         except:
#             return ""
#
#
#
#     def alert(self):
#         try:
#             time.sleep(2)
#             alert = self.driver.switch_to.alert
#             text = alert.text
#             alert.accept()
#             return text
#         except:
#             return ""
#
#
#
#     def test_1(self):
#         self.driver.find_element_by_id("account").send_keys("admin")
#         self.driver.find_element_by_name("password").send_keys("19901201Szy")
#         self.driver.find_element_by_id("submit").click()
#         time.sleep(2)
#         t = self.sucess()
#         print("获取的结果：%s"%t)
#         self.assertTrue(t =="admin")
#
#
#     def test_2(self):
#         self.driver.find_element_by_id("account").send_keys("admin")
#         self.driver.find_element_by_name("password").send_keys("19901201")
#         self.driver.find_element_by_id("submit").click()
#         time.sleep(1)
#         t = self.sucess()
#         print("登录失败，获取的结果：%s"%t)
#         self.assertTrue(t == "")

























from selenium import webdriver
import time
import unittest

class Chandao(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login.html")

    def sucess(self):
        try:
            t = self.driver.find_element_by_css_selector(".user-name").text
            print(t)
            return t
        except:
            return ""

    def alert(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def test_1(self):
        time.sleep(2)
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("19901201Szy")
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)

        t = self.sucess()
        print("获取的结果：%s" % t)
        self.assertTrue(t == "admin")



    def test_2(self):
        time.sleep(2)
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("19901201")
        self.driver.find_element_by_id("submit").click()
        time.sleep(1)

        t = self.sucess()
        print("登录失败，获取的结果：%s" % t)
        self.assertTrue(t == "")



    def tearDown(self):
        self.alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main":
    unittest.main()


























