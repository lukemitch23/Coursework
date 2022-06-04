import mysql.connector

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv

mydb = mysql.connector.connect(
  host="192.168.0.45",
  user="server",
  password="server123",
  database="site"
)

mycursor = mydb.cursor()


lisfile = open('new_list.txt', 'r')

for line in lisfile:
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/lukemitchell/chromedriver', chrome_options=options)
    websitelink = line.strip()
    driver.get(websitelink)
    time.sleep(2)
    try:
        camera = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[2]/div[3]/div').get_attribute('textContent')
        camera_strip = camera.strip()
    except:
        camera_strip = 'Unknown'

    try:
        crop_factor = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[3]/div[3]').get_attribute('textContent')
        crop_factor_strip = crop_factor.strip()
    except:
        crop_factor_strip = 'Unknown'

    try:
        total_megapixels = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[4]/div[3]').get_attribute('textContent')
        total_megapixels_strip = total_megapixels.strip()
    except:
        total_megapixels_strip = 'Unknown'

    try:
        effective_megapixels = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[5]/div[3]').get_attribute('textContent')
        effective_megapixels_strip = effective_megapixels.strip()
    except:
        effective_megapixels_strip = 'Unknown'

    try:
        optical_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[6]/div[3]').get_attribute('textContent')
        optical_zoom_strip = optical_zoom.strip()
    except:
        optical_zoom_strip = 'Unknown'

    try:
        digital_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[7]/div[3]').get_attribute('textContent')
        digital_zoom_strip = digital_zoom.strip()
    except:
        digital_zoom_strip = 'Unknown'

    try:
        iso = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[8]/div[3]').get_attribute('textContent')
        iso_strip = iso.strip()
    except:
        iso_strip = 'Unknown'

    try:
        raw = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[9]/div[3]/span').get_attribute('class')
        raw_strip = raw.strip()
    except:
        raw_strip = 'Unknown'

    try:
        manual_focus = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[10]/div[3]/span').get_attribute('class')
        manual_focus_strip = manual_focus.strip()
    except:
        manual_focus_strip = 'Unknown'

    try:
        focus_range = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[11]/div[3]').get_attribute('textContent')
        focus_range_strip = focus_range.strip()
    except:
        focus_range_strip = 'Unknown'

    try:
        macro_focus_range = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[12]/div[3]').get_attribute('textContent')
        macro_focus_range_strip = macro_focus_range.strip()
    except:
        macro_focus_range_strip = 'Unknown'

    try:
        focal_length = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[13]/div[3]').get_attribute('textContent')
        focal_length_strip = focal_length.strip()
    except:
        focal_length_strip = 'Unknown'

    try:
        aperture_priority = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[14]/div[3]').get_attribute('textContent')
        aperture_priority_strip = aperture_priority.strip()
    except:
        aperture_priority_strip = 'Unknown'

    try:
        max_aperture = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[15]/div[3]').get_attribute('textContent')
        max_aperture_strip = max_aperture.strip()
    except:
        max_aperture_strip = 'Unknown'

    try:
        max_aperture_35 = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[16]/div[3]').get_attribute('textContent')
        max_aperture_35_strip = max_aperture_35.strip()
    except:
        max_aperture_35_strip = 'Unknown'

    try:
        metering = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[17]/div[3]').get_attribute('textContent')
        metering_strip = metering.strip()
    except:
        metering_strip = 'Unknown'

    try:
        exposure_comp = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[18]/div[3]').get_attribute('textContent')
        exposure_comp_strip = exposure_comp.strip()
    except:
        exposure_comp_strip = 'Unknown'

    try:
        shutter_priority = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[19]/div[3]').get_attribute('textContent')
        shutter_priority_strip = shutter_priority.strip()
    except:
        shutter_priority_strip = 'Unknown'

    try:
        min_ss = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[20]/div[3]').get_attribute('textContent')
        min_ss_strip = min_ss.strip()
    except:
        min_ss_strip = 'Unknown'

    try:
        max_ss = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[21]/div[3]').get_attribute('textContent')
        max_ss_strip = max_ss.strip()
    except:
        max_ss_strip = 'Unknown'

    try:
        built_flash = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[22]/div[3]/span').get_attribute('class')
        built_flash_strip = built_flash.strip()
    except:
        built_flash_strip = 'Unknown'

    try:
        external_flash = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[23]/div[3]/span').get_attribute('class')
        external_flash_strip = external_flash.strip()
    except:
        external_flash_strip = 'Unknown'

    try:
        viewfinder = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[24]/div[3]').get_attribute('textContent')
        viewfinder_strip = viewfinder.strip()
    except:
        viewfinder_strip = 'Unknown'

    try:
        white_balance = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[25]/div[3]').get_attribute('textContent')
        white_balance_strip = white_balance.strip()
    except:
        white_balance_strip = 'Unknown'

    try:
        screen_size = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[26]/div[3]').get_attribute('textContent')
        screen_size_strip = screen_size.strip()
    except:
        screen_size_strip = 'Unknown'

    try:
        screen_resolution = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[27]/div[3]').get_attribute('textContent')
        screen_resolution_strip = screen_resolution.strip()
    except:
        screen_resolution_strip = 'Unknown'

    try:
        video = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[28]/div[3]/span').get_attribute('class')
        video_strip = video.strip()
    except:
        video_strip = 'Unknown'

    try:
        video_res = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[29]/div[3]').get_attribute('textContent')
        video_res_strip = video_res.strip()
    except:
        video_res_strip = 'Unknown'

    try:
        storage = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[30]/div[3]').get_attribute('textContent')
        storage_strip = storage.strip()
    except:
        storage_strip = 'Unknown'

    try:
        usb = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[31]/div[3]').get_attribute('textContent')
        usb_strip = usb.strip()
    except:
        usb_strip = 'Unknown'

    try:
        hdmi = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[32]/div[3]/span').get_attribute('class')
        hdmi_strip = hdmi.strip()
    except:
        hdmi_strip = 'Unknown'

    try:
        wireless = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[33]/div[3]/span').get_attribute('class')
        wireless_strip = wireless.strip()
    except:
        wireless_strip = 'Unknown'

    try:
        gps = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[34]/div[3]/span').get_attribute('class')
        gps_strip = gps.strip()
    except:
        gps_strip = 'Unknown'

    try:
        battery = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[35]/div[3]').get_attribute('textContent')
        battery_strip = battery.strip()
    except:
        battery_strip = 'Unknown'

    try:
        weight = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[36]/div[3]').get_attribute('textContent')
        weight_strip = weight.strip()
    except:
        weight_strip = 'Unknown'

    try:
        dimensions = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[37]/div[3]').get_attribute('textContent')
        dimensions_strip = dimensions.strip()
    except:
        dimensions_strip = 'Unknown'

    try:
        year = driver.find_element_by_xpath('//*[@id="main"]/div[22]/div[38]/div[3]').get_attribute('textContent')
        year_strip = year.strip()
    except:
        year_strip = 'Unknown'
    
    print('\n\n', camera_strip, '\n', crop_factor_strip, total_megapixels_strip, effective_megapixels_strip, optical_zoom_strip, digital_zoom_strip, iso_strip, raw_strip, manual_focus_strip, focus_range_strip, macro_focus_range_strip, focal_length_strip, aperture_priority_strip, max_aperture_strip, max_aperture_35_strip, metering_strip, exposure_comp_strip, shutter_priority_strip, min_ss_strip, max_ss_strip, built_flash_strip, external_flash_strip, viewfinder_strip, white_balance_strip, screen_size_strip, screen_resolution_strip, video_strip, video_res_strip, storage_strip, usb_strip, hdmi_strip, wireless_strip, gps_strip, battery_strip, weight_strip, dimensions_strip, year_strip)
    
    query = """INSERT INTO cameras (`camera`,`crop_factor`,`total_megapixels`,`effective_megapixels`,`optical_zoom`,`digital_zoom`,`iso`,`raw`,
    `manual_focus`,`focus_range`,`macro_range`,`focal_length`,`aperture_priority`,`max_aperture`,`35_aperture`,`metering`,`exposure_comp`,
    `shutter_priority`,`min_ss`,`max_ss`,`built_flash`,`external_flash`,`viewfinder`,`white_balance`,`screen_size`,`screen_res`,`video`,
    `video_res`,`storage`,`usb`,`hdmi`,`wireless`,`gps`,`battery`, `weight`, `dimensions`, `year`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    mycursor.execute(query, (camera_strip, crop_factor_strip, total_megapixels_strip, effective_megapixels_strip, optical_zoom_strip, digital_zoom_strip, iso_strip, raw_strip, manual_focus_strip, focus_range_strip, macro_focus_range_strip, focal_length_strip, aperture_priority_strip, max_aperture_strip, max_aperture_35_strip, metering_strip, exposure_comp_strip, shutter_priority_strip, min_ss_strip, max_ss_strip, built_flash_strip, external_flash_strip, viewfinder_strip, white_balance_strip, screen_size_strip, screen_resolution_strip, video_strip, video_res_strip, storage_strip, usb_strip, hdmi_strip, wireless_strip, gps_strip, battery_strip, weight_strip, dimensions_strip, year_strip))
    mydb.commit()
    print('record added for' + camera_strip)