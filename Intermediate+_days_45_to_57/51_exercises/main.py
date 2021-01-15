from json import load
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

MIN_DOWN = 40
MIN_UP = 10
USERNAME = os.getenv('email_user')
PASSWORD = os.getenv('email_token')

class InternetSpeedBot():
    def __init__(self):
        home = Path.home()
        self.driver = webdriver.Chrome(f"{home}/Code/chromedriver")
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        where_input = self.driver.find_element_by_class_name('test-mode-multi')
        where_input.click()
        time.sleep(50)

        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.driver.close()


    def complain(self):
        with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
            connection.starttls()

            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs='marc.falzon@gmail.com',
                msg=f'Subject: Internet Speed\n\nCurrent speed is:\nDown: {self.down}\nUp: {self.up}'.encode('utf-8')
                )
            print('Email sent')


speed_test = InternetSpeedBot()
speed_test.get_internet_speed()
speed_test.complain()