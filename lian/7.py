# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Firefox()
# driver.get("http://boss.xjxueche.com/")
#
#
#
# def findele(driver,locator,timeout=10, t=1):
#     ele = WebDriverWait(driver, timeout, t).until(lambda x: x.find_element(*locator))
#     return  ele
#
# loc1 = (By.ID, "userName")
# loc2 = (By.ID, "password")
# loc3 = (By.CLASS_NAME, "loginBtn")
#
#
# findele(driver,loc1).send_keys("yangqin")
# findele(driver,loc2).send_keys("0406")
# findele(driver,loc3).click()




from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://boss.xjxueche.com/")



def findele(driver, locator, timeout=10, t=1):
    ele = WebDriverWait(driver, timeout, t).until(lambda x: x.find_element(*locator))
    return ele

loc1 = (By.ID, "userName")
loc2 = (By.ID, "password")
loc3 = (By.CLASS_NAME,"loginBtn")

findele(driver,loc1).send_keys("yangqin")
findele(driver,loc2).send_keys("0406")
findele(driver,loc3).click()













