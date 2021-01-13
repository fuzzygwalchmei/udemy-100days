from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv
import time

load_dotenv()


home = Path.home()
chrome_driver = f"{home}/Code/chromedriver"

driver=webdriver.Chrome(chrome_driver)

driver.get('https://au.banggood.com/login.html')

login_entry = driver.find_element_by_name('login-email')
login_entry.send_keys(os.getenv('bg_username'))
passwd_entry = driver.find_element_by_name('login-pwd')
passwd_entry.send_keys(os.getenv('bg_password'))
login_btn  = driver.find_element_by_id('login-submit')
hover = ActionChains(driver).move_to_element(login_btn)
hover.click()

time.sleep(3)

go_to_vip = driver.find_element_by_css_selector('div .info-vip-club a')
hover = ActionChains(driver).move_to_element(go_to_vip)
hover.click()

check_in_hover = driver.find_element_by_class_name('icon-ic-check')
hover = ActionChains(driver).move_to_element(check_in_hover)
hover.perform()

check_in = driver.find_element_by_class_name('check-btn.check.countdown')
hover = ActionChains(driver).move_to_element(check_in)
hover.click()


driver.quit()