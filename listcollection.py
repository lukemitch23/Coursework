from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv

brands = [['canon', '13'],['fujifilm', '16'],['nikon', '12'],['sony', '14'],
    ['leica','3'],['olympus','14'], ['panasonic','10'], ['pentax','6'], 
    ['ricoh','4'], ['samsung','12']]

def url_make(manu, page): 
    manu_string = str(manu)
    page_string = str(page)
    url_maker = "https://www.digicamdb.com/cameras/" + manu_string + "/" + page_string
    driver_get(url_maker)


def driver_get(url):
    global camera_list
    global driver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/lukemitchell/chromedriver', chrome_options=options)
    driver.get(url)
    time.sleep(0.6)
    try:
        for count in range(2,27):
            path = str('//*[@id="main"]/div[2]/div[3]/div['+str(count)+']/div[2]/b/a')
            camera = driver.find_element_by_xpath(path).get_attribute('href')
            file_write(camera)
    except:
        print("Error occured at: " + url)
    driver.close()
    
def file_write(data): 
    lisfile = open('list.csv', 'a')
    lisfile.write(data + '\n')
    lisfile.close()



for a in range(0, len(brands)):
    for b in range(1, int(brands[a][1])):
        print(brands[a][0], b)
        url_make(brands[a][0], b)
