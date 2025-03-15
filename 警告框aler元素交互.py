import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(5)
driver.get("https://sahitest.com/demo/alertTest.htm")
driver.find_element(By.NAME,'b1').click()
time.sleep(2)

#获取弹窗上的文本内容
print(driver.switch_to.alert.text)

#点击弹窗确定
driver.switch_to.alert.accept()
