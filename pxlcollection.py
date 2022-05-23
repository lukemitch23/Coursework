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
driver.maximize_window()

file = open('pxlcollection.csv', 'w')

def x_path(count):
    path = "/html/body/div[1]/div[2]/div[3]/div[1]/span[" + str(count) + "]/a"
    print(path)
    path.strip()
    return path


