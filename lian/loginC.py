# coding:utf-8
# 类和封装


# class Denglu():
#
#
#     def __init__(self, driver):
#         self.driver = driver
#
#
#
#     def login(self, user="admin", pwd="19901201Szy"):
#         self.driver.get("http://127.0.0.1/zentao/user-login.html")
#         self.driver.find_element_by_id("account").send_keys(user)
#         self.driver.find_element_by_name("password").send_keys(pwd)
#         self.driver.find_element_by_id("submit").click()
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
#
#
#
# if __name__ == "__main__":
#
#     from selenium import webdriver
#     import time
#     driver = webdriver.Firefox()
#
#
#
#     chandao = Denglu(driver)
#     chandao.login()





# 封装2
# from selenium import webdriver
# driver = webdriver.Firefox()
# import time
#
#
#
# class Weibo():
#     def __init__(self,driver):
#         self.driver = driver
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
#     def login(self,user="yangqin",pwd="920815"):
#         self.driver.get("http://oa.beidouapp.com/")
#         self.driver.find_element_by_id("login_username").send_keys(user)
#         self.driver.find_element_by_id("login_password").send_keys(pwd)
#         self.driver.find_element_by_id("login_button").click()
#         time.sleep(5)
#
#
#
#
#     def tearDown(self):
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#
#
#
# if __name__ == "__main__":
#     weibo = Weibo(driver)
#     weibo.login()





# # 封装3
# from selenium import webdriver
# driver = webdriver.Firefox()
# import time
#
#
# class Xiaojia():
#     def __init__(self,driver):
#         self.driver = driver
#
#
#
#     def sucess(self):
#          try:
#              t = self.driver.find_element_by_class_name("complex-write").text
#              print(t)
#              return t
#          except:
#              return ""
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
#
#     def login(self,user="yangqin",pwd="0406"):
#         time.sleep(2)
#         self.driver.get("http://boss.xjxueche.com/")
#         self.driver.find_element_by_id("userName").send_keys(user)
#         self.driver.find_element_by_id("password").send_keys(pwd)
#         self.driver.find_element_by_class_name("loginBtn").click()
#         time.sleep(5)
#
#
#
#
#     def tearDown(self):
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#
#
#
# if __name__ == "__main__":
#     xiaojia = Xiaojia(driver)
#     xiaojia.login()





















