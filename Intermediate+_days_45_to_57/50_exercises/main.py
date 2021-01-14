from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time



home = Path.home()
driver = webdriver.Chrome(f"{home}/Code/chromedriver")

driver.get("https://www.speedtest.net/")


where_input = driver.find_element_by_class_name('test-mode-multi')
where_input.click()
time.sleep(50)

dismiss_window = driver.find_element_by_class_name('notification-dismiss')
dismiss_window.click()
