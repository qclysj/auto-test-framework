from selenium import webdriver
from selenium.webdriver.common.by import By
import time
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(5)
driver.get("https://sahitest.com/demo/iframesTest.htm")
#获取iframe元素
driver1=driver.find_element(By.XPATH,'/html/body/iframe')
#进入iframe页面
driver.switch_to.frame(driver1)
driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[1]/a[1]').click()
#退出iframe页面
driver.switch_to.default_content()