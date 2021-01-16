from selenium import webdriver
import os, pathlib
from dotenv import load_dotenv
import selenium



load_dotenv()
home = pathlib.Path.home()
chrome_path = os.getenv('chrome_driver')
driver = webdriver.Chrome(f"{home}{chrome_path}")









driver.quit()