from selenium import webdriver
from selenium.webdriver.common.by import By
import threading#导包

class A1:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def setweb(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=option)
        driver.set_window_size(1000,1000)
        driver.set_window_position(self.x,self.y)
        driver.implicitly_wait(5)
        driver.get("https://bilibili.com")
        return driver
    def getweb(self):
        driver=self.setweb()

        driver.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span').click()
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]").click()

        driver.find_element(By.LINK_TEXT, "电影").click()

        driver1 = driver.window_handles  # 获取全部标签页句柄
        driver.close()
        driver.switch_to.window(driver1[1])  # 切换标签页
s1=A1(0,0)
s2=A1(800,0)
threading.Thread(target=s1.getweb).start()
threading.Thread(target=s2.getweb).start()