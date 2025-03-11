import unittest
from selenium import webdriver
chrome_path=r"D:\应用\chromedriver.exe"
from selenium.webdriver.common.by import  By


class TestCase(unittest.TestCase):
    def test_01_login(self):
        global driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
        driver.get("https://www.jd.com")
        time.sleep(5)
        driver.find_element(By.LINK_TEXT,'立即登录').click()
        driver.find_element(By.ID,'loginname').send_keys('1111111111')
        driver.find_element(By.NAME,'nloginpwd').send_keys('123456789')
        driver.find_element(By.ID,'loginsubmit').click()








