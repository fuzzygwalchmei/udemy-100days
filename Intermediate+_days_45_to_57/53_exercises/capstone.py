import os
import requests
from requests.api import get
import requests_cache
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pathlib import Path
from time import sleep

load_dotenv()


FORM_URL = os.getenv('form_url')


def write_to_sheet(addr, price, website):
    home = Path.home()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(f"{home}/Code/chromedriver", options=options)
    driver.get(FORM_URL)
    sleep(2)
    addr_entry = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr_entry.send_keys(addr)
    price_entry = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_entry.send_keys(price)
    link_entry = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry.send_keys(website)
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit_button.click()
    
    driver.quit()




def get_properties():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    resp = requests.get("https://www.zillow.com/homes/Salinas,-CA_rb/", headers=headers)
    resp.raise_for_status()
    page = BeautifulSoup(resp.text, 'html.parser')


    listings = page.find_all("div", class_="list-card-info")
    for list in listings[:2]:
        addr = list.find(class_='list-card-addr').get_text()
        price = list.find(class_='list-card-price').get_text()
        website = list.find(class_='list-card-link')['href']

        write_to_sheet(addr, price, website)


get_properties()