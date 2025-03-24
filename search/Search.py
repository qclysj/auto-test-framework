import time

from selenium.webdriver.common.by import By



def Search(driver):

    time.sleep(10)
    driver.find_element(By.ID,'key').click()
    time.sleep(2)
    driver.find_element(By.ID,'key').send_keys("iphone16promax")
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,'button').click()
