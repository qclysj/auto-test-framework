import time
from selenium import webdriver
from selenium.webdriver.common.by import By



#获取浏览器对象，以京东为例

#进行登录操作
class Login:
    def webdriver(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=option)
        driver.get("https://www.jd.com")
        #等待小广告
        time.sleep(8)
        return driver
    def login(self):

        driver=self.webdriver()

        driver.find_element(By.LINK_TEXT,"立即登录").click()
        driver.find_element(By.ID,"loginname").send_keys('yourusername')
        driver.find_element(By.ID,"nloginpwd").send_keys('yourpassword')
        driver.find_element(By.ID,"loginsubmit").click()
        ##!!!滑块验证码手动操作
        return driver
