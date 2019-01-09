# 判断元素是隐藏还是显示的
from selenium import webdriver
from common.base import Base


driver = webdriver.Firefox()
driver.get("http://boss.xjxueche.com/")
xiaojia = Base(driver)

loc1 = ("id","userName")

# 判断元素
a = xiaojia.findElement(loc1)
r = a.is_displayed()
print(r)
# True:显示的,  False:隐藏的,   元素不存在报错




# is_selccted()判断是够被选中，返回True和False(针对下拉框)








