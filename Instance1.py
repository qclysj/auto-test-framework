from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get('https://bilibili.com')
driver.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span').click()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT,"电影").click()


driver1=driver.window_handles#获取全部标签页句柄
driver.close()
driver.switch_to.window(driver1[1])#切换标签页
driver1=driver.current_window_handle#获取当前标签页句柄
