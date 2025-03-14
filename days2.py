#进框架driver.switch_to.frame
#出框架driver.switch_to.default_content()
from selenium import webdriver#操作浏览器
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)#保持浏览器打开
driver = webdriver.Chrome(options=option)
option.add_argument('--no-sandbox')#增加兼容性
driver.get("https://baidu.com")
# driver.close()#关闭当前页面
# driver.quit()#关闭浏览器

# driver.maximize_window()#浏览器最大化
# driver.minimize_window()#浏览器最小化

# driver.set_window_position(200,0)#控制浏览器打开位置
# driver.set_window_size(1,1)#控制浏览器尺寸

# driver.get_screenshot_as_file('1.png')#浏览器截图
# driver.refresh()#刷新当前网页

