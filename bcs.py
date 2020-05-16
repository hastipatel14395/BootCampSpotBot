from splinter import Browser
from selenium import webdriver
import credentials
import time
from selenium.webdriver.chrome.options import Options
from credentials import username
from credentials import password


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url= 'http://bootcampspot.com/'

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get(url)



driver.find_element_by_id('emailAddress').send_keys(username)
driver.find_element_by_id('password').send_keys(password)

time.sleep(2)

driver.find_element_by_xpath('//*[@id="root"]/section/div/div[2]/button').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="main-content"]/div/section/div/div[3]/div/div[3]/ul/li[1]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="take-attendance"]').click()
#signs back out of BCS for safety purposes
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/header/nav/ul/li[4]/a').click()