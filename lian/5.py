# coding:utf-8
# from selenium import webdriver
# import time
# import unittest
#
# class Chandao(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#
#     def setUp(self):
#         self.driver.get("http://127.0.0.1/zentao/user-login.html")
#
#
#     def success(self):
#         try:
#             t = self.driver.find_element_by_css_selector(".user-name").text
#             print(t)
#             return t
#         except:
#             return ""
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
#     def test_1(self):
#         time.sleep(2)
#         self.driver.find_element_by_id("account").send_keys("YQQ")
#         self.driver.find_element_by_name("password").send_keys("19901201Szy")
#         self.driver.find_element_by_id("submit").click()
#         time.sleep(2)
#
#         t = self.success()
#         print("登录成功，获取的结果是 %s"%t)
#         self.assertTrue(t =="YQQ")
#
#
#
#     def test_2(self):
#         time.sleep(2)
#         self.driver.find_element_by_id("account").send_keys("YQQ")
#         self.driver.find_element_by_name("password").send_keys("19901201")
#         self.driver.find_element_by_id("submit").click()
#         time.sleep(2)
#
#         t = self.success()
#         print("登录失败，获取的结果是 %s" % t)
#         self.assertTrue(t == "")
#
#
#     def tearDown(self):
#         self.alert()
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#         unittest.main()










# 封装结果
# from selenium import webdriver
# import time
# import unittest
# from lian.loginC import Denglu
#
# class LoginTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#         cls.chandao = Denglu(cls.driver)
#
#     def setUp(self):
#         self.driver.get("http://127.0.0.1/zentao/user-login.html")
#
#
#
#     def test_1(self):
#         time.sleep(5)
#         self.chandao.login("admin","19901201Szy")
#         time.sleep(5)
#
#
#         t = self.chandao.success()
#         print("登录成功，获取的结果是 %s"%t)
#         self.assertTrue(t =="YQQ")
#
#
#
#     def test_2(self):
#         time.sleep(2)
#         self.chandao.login("admin", "1990120")
#         time.sleep(2)
#
#         t = self.chandao.success()
#         print("登录失败，获取的结果是 %s" % t)
#         self.assertTrue(t == "")
#
#
#     def tearDown(self):
#         self.chandao.alert()
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#         unittest.main()



















# 封装2，源码：
# from selenium import webdriver
# import time
# import unittest
#
#
# class Weibo(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#
#     def setUp(self):
#         self.driver.get("http://oa.beidouapp.com/")
#
#
#     def sucess(self):
#         try:
#             t = self.driver.find_element_by_id("accountNameDiv").text
#             print(t)
#             return t
#         except:
#             return ""
#
#
#     def alert(self):
#         try:
#             alert = self.driver.switch_to.alert()
#             text = alert.text()
#             alert.accept()
#             return text
#         except:
#             return ""
#
#
#
#     def test_1(self):
#         time.sleep(3)
#         self.driver.find_element_by_id("login_username").send_keys("yangqin")
#         self.driver.find_element_by_id("login_password").send_keys("920815")
#         self.driver.find_element_by_id("login_button").click()
#         time.sleep(5)
#
#
#         t = self.sucess()
#         print("登录成功，获得的结果是 %s"%t)
#         self.assertTrue(t == "易通星云（北京）科技发展有限公司")
#
#     def test_2(self):
#         time.sleep(3)
#         self.driver.find_element_by_id("login_username").send_keys("yangqin")
#         self.driver.find_element_by_id("login_password").send_keys("92")
#         self.driver.find_element_by_id("login_button").click()
#         time.sleep(5)
#
#         t = self.sucess()
#         print("登录失败，获得的结果是 %s" % t)
#         self.assertTrue(t == "")
#
#
#
#     def tearDown(self):
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()









# 封装2
# from selenium import webdriver
# import time
# import unittest
# from lian.loginC import Weibo
#
#
# class Login(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#         cls.weibo = Weibo(cls.driver)
#
#     def setUp(self):
#         self.driver.get("http://oa.beidouapp.com/")
#
#
#
#
#     def test_1(self):
#         time.sleep(3)
#         self.weibo.login("yangqin","920815")
#
#         t = self.weibo.sucess()
#         print("登录成功，获得的结果是 %s"%t)
#         self.assertTrue(t == "易通星云（北京）科技发展有限公司")
#
#     def test_2(self):
#         time.sleep(3)
#         self.weibo.login("yangqin","92")
#         time.sleep(5)
#
#         t = self.weibo.sucess()
#         print("登录失败，获得的结果是 %s" % t)
#         self.assertTrue(t == "")
#
#
#
#     def tearDown(self):
#         self.weibo.alert()
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()








# 封装3


# from selenium import webdriver
# import time
# import unittest
# from lian.loginC import Xiaojia
#
# class Login(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#         cls.xiaojia = Xiaojia(cls.driver)
#
#     def setUp(self):
#         self.driver.get("http://boss.xjxueche.com/")
#
#
#
#     def test_1(self):
#         time.sleep(2)
#         self.xiaojia.login("yangqin","0406")
#         time.sleep(5)
#
#         t = self.xiaojia.sucess()
#         print("登录成功，获得的结果是%s"%t)
#         self.assertTrue(t == "设备管理")
#
#
#
#     def test_2(self):
#         time.sleep(2)
#         self.xiaojia.login("yangqin","040")
#
#         t = self.xiaojia.sucess()
#         print("登录失败，获得的结果是%s" % t)
#         self.assertTrue(t == "")
#
#
#     def tearDown(self):
#         self.xiaojia.alert()
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
#







