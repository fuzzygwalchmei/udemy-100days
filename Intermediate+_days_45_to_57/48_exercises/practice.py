
from selenium import webdriver
import pathlib

home = pathlib.Path.home()

# Requires chromedriver file to a folder named Code in the users home folder
chrome_driver = f'{home}/Code/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
page_count = driver.find_element_by_css_selector('#articlecount a')
print(page_count.text)


driver.quit()