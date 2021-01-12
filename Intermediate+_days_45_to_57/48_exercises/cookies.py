from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pathlib
import time

home = pathlib.Path.home()

driver = webdriver.Chrome(executable_path=f"{home}/Code/chromedriver")

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element_by_id('cookie')

timeout = time.time() + 5

while True:
    cookie_button.click()
    if time.time() > timeout:
        timeout = time.time() + 5
        prices = driver.find_elements_by_css_selector('#store b')
        for price in prices:
            print(price.text)
