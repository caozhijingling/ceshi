# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://127.0.0.1/zentao/user-login.html")
time.sleep(2)

driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("19901201Szy")
driver.find_element_by_id("keepLoginon").click()
driver.find_element_by_id("submit").click()
time.sleep(2)


t = driver.find_element_by_id("userNav").text
print("admin")

if t == "admin":
    print('登录成功')
else:
    print('登录失败')




























