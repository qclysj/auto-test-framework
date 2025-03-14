from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get('https://www.baidu.com/')
# driver.find_element(By.ID,'kw').send_keys('刘强东')#                   id定位
# driver.find_element(By.NAME,'wd').send_keys('京东')#                   name定位
# driver.find_element(By.LINK_TEXT,'新闻').click()#                      link_text定位
# driver.find_element(By.PARTIAL_LINK_TEXT,'新').click()#                partail_link_text定位





#xpath定位：/开头是绝对路径，//开头是相对路径（常和索引、属性、通配符、部分属性值、文本）
# driver.find_element(By.XPATH,'//form/span[1]/input').send_keys('华为')#索引
# driver.find_element(By.XPATH,"//input[@autocomplete='off']").send_keys('华为')#属性
# driver.find_element(By.XPATH,"//*[@autocomplete='off']").send_keys('华为')#通配符
# driver.find_element(By.XPATH,"//*[starts-with(@autocomplete,'of')]").send_keys('华为')#部分属性值:以什么开头
# driver.find_element(By.XPATH,"//*[substring(@autocomplete,2)='ff']").send_keys('华为')#部分属性值：以什么结尾
# driver.find_element(By.XPATH,"//*[contains(@autocomplete,'of')]").send_keys('华为')#部分属性值：包含
'''
value=driver.find_element(By.XPATH,"//span[text()='按图片搜索']").get_attribute('class')#文本
print(value)
'''
#class_name定位：class值不能有空格，否则报错
# driver.find_element(By.CLASS_NAME,'entry-title').click()
# driver.find_elements(By.CLASS_NAME,'channel-icons__item')[1].click()


#tag_name定位
# driver.find_element(By.TAG_NAME,'input').click()


# css定位：通过id和class定位，通过属性定位，部分属性定位，查询子元素定位，查询兄弟节点定位
# #1.#id=井号+id值 通过id定位
# driver.find_element(By.CSS_SELECTOR,'#kw')
# #2..class=点+class值 通过class定位
# driver.find_element(By.CSS_SELECTOR,'.s_ipt')
# #3.不加修饰符=标签头 通过标签头定位
# driver.find_elements(By.CSS_SELECTOR,'input')[7]
#4.通过任意类型定位[类型=精准值][类型*=模糊值][类型^=开头值][类型值$=结束值]
#or 点击浏览器右键复制selector
driver.find_element(By.CSS_SELECTOR,"[autocomplete='off']").send_keys('1')
