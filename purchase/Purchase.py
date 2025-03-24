import time

from selenium.webdriver.common.by import By

def Purchase(driver):
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div").click()
    driver1 = driver.window_handles  # 获取全部标签页句柄
    driver.switch_to.window(driver1[1])  # 切换标签页
    driver1 = driver.current_window_handle  # 获取当前标签页句柄
