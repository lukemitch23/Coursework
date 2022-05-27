from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import *
import time
import csv
import pyautogui as pg

page_url = "https://pxlmag.com/db/camera-search"

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome('/Users/lukemitchell/chromedriver', chrome_options=options)
driver.get(page_url)
time.sleep(10)
print("\n page loaded \n")
driver.find_element_by_class_name("fc-button fc-cta-consent fc-primary-button").click()
print("\n Element should be clicked \n")


file = open('pxlcollection.csv', 'w')

def x_path(count):
    path = "/html/body/div[1]/div[2]/div[3]/div[1]/span[" + str(count) + "]/a"
    print(path)
    path.strip()
    return path

def spec(camera):
    fullurl = camera + "#Specifications"
    fullurl.strip()
    return fullurl


for i in range(1,7):
    find_path = x_path(i)
    camera = driver.find_element_by_xpath(find_path).get_attribute('href')
    file.write(spec(camera) + '\n')
    print(camera)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/button[2]").click()
    print("next page clicked")
    time.sleep(2)

for i in range(1,7):
    find_path = x_path(i)
    camera = driver.find_element_by_xpath(find_path).get_attribute('href')
    file.write(spec(camera) + '\n')
    print(camera)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/button[2]").click()
    print("next page clicked")
    time.sleep(2)