# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
#
# class Base():
#
#     def __init__(self,driver):
#         self.driver = driver
#         self.timeout = 10
#         self.t = 1
#
#     def findElement(self,locator):
#         ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
#         return ele
#
#     def sendKeys(self,locator,text):
#         ele = self.findElement(locator)
#         ele.send_keys(text)
#
#     def click(self,locator):
#         ele = self.findElement(locator)
#         ele.click()
#
#     def clear(self,locator):
#         ele = self.findElement(locator)
#         ele.clear()
#
# if __name__ == "__main__":
#     driver = webdriver.Firefox()
#     driver.get("http://boss.xjxueche.com/")
#     xiaojia = Base(driver)
#
#     loc1 = ("id","userName")
#     loc2 = ("id", "password")
#     loc3 = ("class name", "loginBtn")
#
#     xiaojia.sendKeys( loc1,"yangqin")
#     xiaojia.sendKeys(loc2,"0406")
#     xiaojia.click(loc3)







from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 1


    # def findElementNew(self, locator):
    #     ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
    #     return  ele


    def findElement(self,locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele


    def sendkeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)


    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()


    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()


    def get_text(self, locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("登录失败，返回‘’")
            return ""

    def is_element_exist(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False


    def move_to_element(self,locator):
        '''封装鼠标事件'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()



    def select_by_index(self, locator, index=0):
        '''通过索引，index是索引第几个，从0开始默认为第一个'''
        ele = self.findElement(locator)
        Select(ele).select_by_index(index)



    def select_by_value(self, locator, value):
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)



    def select_by_text(self, locator, text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)






    # def isSelected(self,locator):
    #     ele = self.findElement(locator)
    #     r = ele.is_selected()
    #     return r


    #
    # def isElementExist2(self,locator):
    #     eles = self.findElement(locator)
    #     n = len(eles)
    #     if n ==0:
    #         return  False
    #     elif n == 1:
    #         return  True
    #     else:
    #         return  True
    #
    # def is_title(self,_title):
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
    #         return result
    #     except:
    #         return False
    #
    #
    # def is_title_contains(self, _title):
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
    #         return result
    #     except:
    #         return False
    #
    #
    # def is_text_in_element(self,locator,_text):
    #     try:
    #         result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
    #         return result
    #     except:
    #         return False







if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://boss.xjxueche.com/")
    xiaojia = Base(driver)

    loc1 = ("id","userName")
    loc2 = ("id", "password")
    loc3 = ("class name", "loginBtn")

    xiaojia.sendkeys( loc1,"yangqin")
    xiaojia.sendkeys(loc2,"0406")
    xiaojia.click(loc3)






