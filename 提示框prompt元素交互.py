from selenium import webdriver
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(5)
driver.get("https://sahitest.com/demo/promptTest.htm")
driver.find_element(By.NAME,'b1').click()

driver.switch_to.alert.send_keys('天下无双')


#点击弹窗确定
driver.switch_to.alert.accept()
