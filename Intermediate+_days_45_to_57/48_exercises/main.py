
from selenium import webdriver
import pathlib
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


home = pathlib.Path.home()

# Requires chromedriver file to a folder named Code in the users home folder
chrome_driver = f'{home}/Code/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)

# driver.get('https://www.amazon.com.au/Exploding-Kittens-Card-Game-Family-Friendly/dp/B0825N5Y7V/')
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

# xpath_price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]')

# print(xpath_price.text)

# driver.get("https://www.python.org")
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")


# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "times" : event_times[n].text,
#         "name" : event_names[n].text
#     }

# print(events)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # all_portals = driver.find_element_by_link_text('All portals')
# # all_portals.click()

# search = driver.find_element_by_name('search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com")
fname = driver.find_element_by_name('fName')
fname.send_keys('Marc')
lname = driver.find_element_by_name('lName')
lname.send_keys('Falzon')
email = driver.find_element_by_name('email')
email.send_keys('marc.falzon@gmail.com')
email.send_keys(Keys.ENTER)



# driver.quit()
