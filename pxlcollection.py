from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import *
import time
import csv

page_url = "https://pxlmag.com/db/camera-search"

#options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome('/Users/lukemitchell/chromedriver')#, chrome_options=options)
driver.get(page_url)

file = open('pxlcollection.csv', 'w')

def x_path(count):
    path = "/html/body/div[1]/div[2]/div[3]/div[1]/span[" + str(count) + "]/a"
    print(path)
    path.strip()
    return path

for b in range(1,35):
    print("b=" + str(b))
    for i in range (1,36):
        print("i=" + str(i))
        path = x_path(i)
        time.sleep(2)
        camera = driver.find_element_by_xpath(path).get_attribute('href')
        full_camera = camera + "#Specifications"
        fc_strip = full_camera.strip()
        file.write(fc_strip + "\n")
        print("written to file")
        time.sleep(0.5)
    time.sleep(5)
    next_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/button[2]')
    next_button.click()
    print("next page")

file.close()