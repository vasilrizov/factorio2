from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\vasilpc\\PycharmProjects\\untitled1\\driver\\chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get("http://google.bg")
driver.find_element_by_name("q").send_keys("it works")
driver.find_element_by_class_name("gNO89b").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()