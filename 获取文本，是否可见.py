from selenium import webdriver
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(5)
driver.get("https://h.xinhuaxmt.com/vh512/share/12446375?newstype=1001&homeshow=1")
a=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[3]/div[2]/section/p[1]').text

print(a)
#是否可见
a1=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[3]/div[2]/section/p[1]').is_displayed()
print(a1)