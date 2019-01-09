# 登录函数的用法


# def login(driver,user="admin",pwd="19901201Szy"):
#     driver.get("http://127.0.0.1/zentao/user-login.html")
#     driver.find_element_by_id("account").send_keys(user)
#     driver.find_element_by_name("password").send_keys(pwd)
#     driver.find_element_by_id("submit").click()
#
# if __name__ == "__main__":
#
#     from selenium import webdriver
#     driver = webdriver.Firefox()
#     login(driver)










# def login(driver,user="admin",pwd="19901201Szy"):
#     driver.get("http://127.0.0.1/zentao/user-login.html")
#     driver.find_element_by_id("account").send_keys(user)
#     driver.find_element_by_name("password").send_keys(pwd)
#     driver.find_element_by_id("submit").click()
#
# if __name__ == "__main__":
#
#     from selenium import webdriver
#     driver = webdriver.Firefox()
#     login(driver,"YQQ","19901201Szy")








# 案列1
# def login(driver,user="admin",pwd="19901201Szy"):
#     driver.get("http://127.0.0.1/zentao/user-login.html")
#     driver.find_element_by_id("account").send_keys(user)
#     driver.find_element_by_name("password").send_keys(pwd)
#     driver.find_element_by_id("submit").click()





# 案列2
def login(driver,user="admin",pwd="19901201Szy"):
    driver.get("http://127.0.0.1/zentao/user-login.html")
    driver.find_element_by_id("account").send_keys(user)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_id("submit").click()
















