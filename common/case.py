from selenium import webdriver
from common.base import Base
import  time
url = "http://127.0.0.1/zentao/user-login.html"

class Login_page(Base):

    loc_user = ("id", "account")
    loc_pwd = ("name", "password")
    loc_keep_login = ("id", "keepLoginon")
    loc_login = ("id", "submit")
    loc_forget_pwd = ("link text", "忘记密码")
    loc_get_user = ("id", "userNav")
    loc_forget_pwd_page = ("xpath", "html/body/div[1]/div/div[2]/div[2]/a")


    def input_user(self, text):
        self.sendkeys(self.loc_user,text)

    def input_pwd(self, text):
        self.sendkeys(self.loc_pwd, text)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    def click_login(self):
        self.click(self.loc_login)

    def click_forget_pwd(self):
        self.click(self.loc_forget_pwd)

    def get_login_user(self):
        user = self.get_text(self.loc_get_user)
        return user

    def is_alert(self):
        '''判断弹窗是不是在'''
        try:
            time.sleep(3)
            alert = self.driver.swich_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def is_fresh_exit(self):
        '''判断忘记密码页，刷新按钮是否在'''
        r = self.is_element_exist(self.loc_forget_pwd_page)
        return r





if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_page = Login_page(driver)
    driver.get(url)
    login_page.input_user("admin")
    login_page.input_pwd("19901201Szy")
    login_page.click_keep_login()
    login_page.click_login()