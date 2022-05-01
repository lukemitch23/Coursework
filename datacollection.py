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


lisfile = open('list.txt', 'r')
#sparefile = open('spare.csv', 'w')

def get_url(k):
  address = lisfile.readline(k)
  print(address)
  return address

def knownas_dop():
  try:
    brand = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[1]/td[2]/a').get_attribute("textContent")
    brand_strip=brand.strip()
  except:
    brand_strip = "unknown"
  try:
    camera_model = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[2]/td[2]').get_attribute("textContent")
    camera_model_strip=camera_model.strip()
  except:
    camera_model_strip = "unknown"
  try:
    megapixels = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
    megapixels_strip=megapixels.strip()
  except:
    megapixels_strip = "unknown"
  try:
    sensor_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[6]/td[2]').get_attribute("textContent")
    sensor_size_strip=sensor_size.strip()
  except:
    sensor_size_strip = "unknown"
  try:
    sensor_type = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[7]/td[2]').get_attribute("textContent")
    sensor_type_strip=sensor_type.strip()
  except:
    sensor_type_strip = "unknown"
  try:
    crop_factor = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[10]/td[2]').get_attribute("textContent")
    crop_factor_strip=crop_factor.strip()
  except:
    crop_factor_strip = "unknown"
  try:
    optical_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[11]/td[2]').get_attribute("textContent")
    optical_zoom_strip=optical_zoom.strip()
  except:
    optical_zoom_strip = "unknown"
  try:
    digital_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[12]/td[2]').get_attribute("textContent")
    digital_zoom_strip=digital_zoom.strip()
  except:
    digital_zoom_strip = "unknown"
  try:
    iso = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[13]/td[2]').get_attribute("textContent")
    iso_strip=iso.strip()
  except:
    iso_strip = "unknown"
  try:
    raw = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[14]/td[2]').get_attribute('class')
    raw_strip=raw.strip()
  except:
    raw_strip = "unknown"
  try:
    manual_focus = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[15]/td[2]/span').get_attribute('class')
    manual_focus_strip=manual_focus.strip()
  except:
    manual_focus_strip = "unknown"
  try:
    focus_range = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[16]/td[2]').get_attribute("textContent")
    focus_range_strip=focus_range.strip()
  except:
    focus_range_strip = "unknown"
  try:
    focal_length = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[18]/td[2]').get_attribute("textContent")
    focal_length_strip=focal_length.strip()
  except:
    focal_length_strip = "unknown"
  try:
    aperture_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[19]/td[2]').get_attribute("textContent")
    aperture_priority_strip=aperture_priority.strip()
  except:
    aperture_priority_strip = "unknown"
  try:
    max_aperture = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[20]/td[2]').get_attribute("textContent")
    max_aperture_strip=max_aperture.strip()
  except:
    max_aperture_strip = "unknown"
  try:
    metering = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[23]/td[2]').get_attribute("textContent")
    metering_strip=metering.strip()
  except:
    metering_strip = "unknown"
  try:
    exposure_comp = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[24]/td[2]').get_attribute("textContent")
    exposure_comp_strip=exposure_comp.strip()
  except:
    exposure_comp_strip = "unknown"
  try:
    shutter_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[25]/td[2]').get_attribute("textContent")
    shutter_priority_strip=shutter_priority.strip()
  except:
    shutter_priority_strip = "unknown"
  try:
    min_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[26]/td[2]').get_attribute("textContent")
    min_ss_strip=min_ss.strip()
  except:
    min_ss_strip = "unknown"
  try:
    max_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[27]/td[2]').get_attribute("textContent")
    max_ss_strip=max_ss.strip()
  except:
    max_ss_strip = "unknown"
  try:
    built_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[28]/td[2]/span').get_attribute('class')
    built_flash_strip=built_flash
  except:
    built_flash_strip = "unknown"
  try:
    external_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[29]/td[2]/span').get_attribute("textContent")
    external_flash_strip=external_flash.strip()
  except:
    external_flash_strip = "unknown"
  try:
    viewfinder = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[30]/td[2]').get_attribute("textContent")
    viewfinder_strip=viewfinder.strip()
  except:
    viewfinder_strip = "unknown"
  try:
    whitebalance = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[31]/td[2]').get_attribute("textContent")
    whitebalance_strip=whitebalance.strip()
  except:
    whitebalance_strip = "unknown"
  try:
    screen_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[32]/td[2]').get_attribute("textContent")
    screen_size_strip=screen_size.strip()
  except:
    screen_size_strip = "unknown"
  try:
    screen_res = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[33]/td[2]').get_attribute("textContent")
    screen_res_strip=screen_res.strip()
  except:
    screen_res_strip = "unknown"
  try:
    video = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[34]/td[2]/span').get_attribute('class')
    video_strip=video
  except:
    video_strip = "unknown"
  try:
    storage = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[36]/td[2]').get_attribute("textContent")
    storage_strip=storage.strip()
  except:
    storage_strip = "unknown"
  try:
    battery = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[41]/td[2]').get_attribute("textContent")
    battery_strip=battery.strip()
  except:
    battery_strip = "unknown"
  try:
    weight = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[42]/td[2]').get_attribute("textContent")
    weight_strip=weight.strip()
  except:
    weight_strip = "unknown"
  try:
    dimensions = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[43]/td[2]').get_attribute("textContent")
    dimensions_strip=dimensions.strip()
  except:
    dimensions_strip = "unknown"
  try:
    year = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[44]/td[2]').get_attribute("textContent")
    year_strip=year.strip()
  except:
    year_strip = "unknown"

  query = """INSERT INTO cameras (`brand`,`model`,`megapixels`,`sensor_size`,`sensor_type`,`crop_factor`,`optical_zoom`,`digital_zoom`,`iso`,
  `raw`,`manual_focus`,`focus_range`,`focal_length`,`aperture_priority`,`max_aperature`,`metering`,`exposure_comp`,`shutter_priority`,
  `min_ss`,`max_ss`,`built_flash`,`external_flash`,`viewfinder`,`whitebalance`,`screen_size`,`screen_res`,`video`,`storage`,
  `battery`,`weight`,`dimension`,`year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
  mycursor.execute(query, (brand_strip, camera_model_strip, megapixels_strip, sensor_size_strip, sensor_type_strip, crop_factor_strip, optical_zoom_strip, digital_zoom_strip, iso_strip, raw_strip, manual_focus_strip, focus_range_strip, focal_length_strip, aperture_priority_strip, max_aperture_strip, metering_strip, exposure_comp_strip, shutter_priority_strip, min_ss_strip, max_ss_strip, built_flash_strip, external_flash_strip, viewfinder_strip, whitebalance_strip, screen_size_strip, screen_res_strip, video_strip, storage_strip, battery_strip, weight_strip, dimensions_strip, year_strip))
  mydb.commit()
  print('record added for' + camera_model_strip)

def knownas():
  try:
    brand = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[1]/td[2]/a').get_attribute("textContent")
    brand_strip=brand.strip()
  except:
    brand_strip = "unknown"
  try:
    camera_model = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[2]/td[2]').get_attribute("textContent")
    camera_model_strip=camera_model.strip()
  except:
    camera_model_strip = "unknown"
  try:
    megapixels = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
    megapixels_strip=megapixels.strip()
  except:
    megapixels_strip = "unknown"
  try:
    sensor_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[6]/td[2]').get_attribute("textContent")
    sensor_size_strip=sensor_size.strip()
  except:
    sensor_size_strip = "unknown"
  try:
    sensor_type = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[7]/td[2]').get_attribute("textContent")
    sensor_type_strip=sensor_type.strip()
  except:
    sensor_type_strip = "unknown"
  try:
    crop_factor = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[10]/td[2]').get_attribute("textContent")
    crop_factor_strip=crop_factor.strip()
  except:
    crop_factor_strip = "unknown"
  try:
    optical_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[11]/td[2]').get_attribute("textContent")
    optical_zoom_strip=optical_zoom.strip()
  except:
    optical_zoom_strip = "unknown"
  try:
    digital_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[12]/td[2]').get_attribute("textContent")
    digital_zoom_strip=digital_zoom.strip()
  except:
    digital_zoom_strip = "unknown"
  try:
    iso = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[13]/td[2]').get_attribute("textContent")
    iso_strip=iso.strip()
  except:
    iso_strip = "unknown"
  try:
    raw = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[14]/td[2]').get_attribute('class')
    raw_strip=raw.strip()
  except:
    raw_strip = "unknown"
  try:
    manual_focus = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[15]/td[2]/span').get_attribute('class')
    manual_focus_strip=manual_focus.strip()
  except:
    manual_focus_strip = "unknown"
  try:
    focus_range = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[16]/td[2]').get_attribute("textContent")
    focus_range_strip=focus_range.strip()
  except:
    focus_range_strip = "unknown"
  try:
    focal_length = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[18]/td[2]').get_attribute("textContent")
    focal_length_strip=focal_length.strip()
  except:
    focal_length_strip = "unknown"
  try:
    aperture_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[19]/td[2]').get_attribute("textContent")
    aperture_priority_strip=aperture_priority.strip()
  except:
    aperture_priority_strip = "unknown"
  try:
    max_aperture = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[20]/td[2]').get_attribute("textContent")
    max_aperture_strip=max_aperture.strip()
  except:
    max_aperture_strip = "unknown"
  try:
    metering = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[22]/td[2]').get_attribute("textContent")
    metering_strip=metering.strip()
  except:
    metering_strip = "unknown"
  try:
    exposure_comp = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[23]/td[2]').get_attribute("textContent")
    exposure_comp_strip=exposure_comp.strip()
  except:
    exposure_comp_strip = "unknown"
  try:
    shutter_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[24]/td[2]').get_attribute("textContent")
    shutter_priority_strip=shutter_priority.strip()
  except:
    shutter_priority_strip = "unknown"
  try:
    min_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[25]/td[2]').get_attribute("textContent")
    min_ss_strip=min_ss.strip()
  except:
    min_ss_strip = "unknown"
  try:
    max_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[26]/td[2]').get_attribute("textContent")
    max_ss_strip=max_ss.strip()
  except:
    max_ss_strip = "unknown"
  try:
    built_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[27]/td[2]/span').get_attribute('class')
    built_flash_strip=built_flash
  except:
    built_flash_strip = "unknown"
  try:
    external_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[28]/td[2]/span').get_attribute("textContent")
    external_flash_strip=external_flash.strip()
  except:
    external_flash_strip = "unknown"
  try:
    viewfinder = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[29]/td[2]').get_attribute("textContent")
    viewfinder_strip=viewfinder.strip()
  except:
    viewfinder_strip = "unknown"
  try:
    whitebalance = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[30]/td[2]').get_attribute("textContent")
    whitebalance_strip=whitebalance.strip()
  except:
    whitebalance_strip = "unknown"
  try:
    screen_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[31]/td[2]').get_attribute("textContent")
    screen_size_strip=screen_size.strip()
  except:
    screen_size_strip = "unknown"
  try:
    screen_res = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[32]/td[2]').get_attribute("textContent")
    screen_res_strip=screen_res.strip()
  except:
    screen_res_strip = "unknown"
  try:
    video = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[33]/td[2]/span').get_attribute('class')
    video_strip=video
  except:
    video_strip = "unknown"
  try:
    storage = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[35]/td[2]').get_attribute("textContent")
    storage_strip=storage.strip()
  except:
    storage_strip = "unknown"
  try:
    battery = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[40]/td[2]').get_attribute("textContent")
    battery_strip=battery.strip()
  except:
    battery_strip = "unknown"
  try:
    weight = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[41]/td[2]').get_attribute("textContent")
    weight_strip=weight.strip()
  except:
    weight_strip = "unknown"
  try:
    dimensions = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[42]/td[2]').get_attribute("textContent")
    dimensions_strip=dimensions.strip()
  except:
    dimensions_strip = "unknown"
  try:
    year = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[43]/td[2]').get_attribute("textContent")
    year_strip=year.strip()
  except:
    year_strip = "unknown"

  query = """INSERT INTO cameras (`brand`,`model`,`megapixels`,`sensor_size`,`sensor_type`,`crop_factor`,`optical_zoom`,`digital_zoom`,`iso`,
  `raw`,`manual_focus`,`focus_range`,`focal_length`,`aperture_priority`,`max_aperature`,`metering`,`exposure_comp`,`shutter_priority`,
  `min_ss`,`max_ss`,`built_flash`,`external_flash`,`viewfinder`,`whitebalance`,`screen_size`,`screen_res`,`video`,`storage`,
  `battery`,`weight`,`dimension`,`year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
  mycursor.execute(query, (brand_strip, camera_model_strip, megapixels_strip, sensor_size_strip, sensor_type_strip, crop_factor_strip, optical_zoom_strip, digital_zoom_strip, iso_strip, raw_strip, manual_focus_strip, focus_range_strip, focal_length_strip, aperture_priority_strip, max_aperture_strip, metering_strip, exposure_comp_strip, shutter_priority_strip, min_ss_strip, max_ss_strip, built_flash_strip, external_flash_strip, viewfinder_strip, whitebalance_strip, screen_size_strip, screen_res_strip, video_strip, storage_strip, battery_strip, weight_strip, dimensions_strip, year_strip))
  mydb.commit()
  print('record added for' + camera_model_strip)

def regular_dop():
  try:
    brand = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[1]/td[2]/a').get_attribute("textContent")
    brand_strip=brand.strip()
  except:
    brand_strip = "unknown"
  try:
    camera_model = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[2]/td[2]').get_attribute("textContent")
    camera_model_strip=camera_model.strip()
  except:
    camera_model_strip = "unknown"
  try:
    megapixels = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[4]/td[2]').get_attribute("textContent")
    megapixels_strip=megapixels.strip()
  except:
    megapixels_strip = "unknown"
  try:
    sensor_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
    sensor_size_strip=sensor_size.strip()
  except:
    sensor_size_strip = "unknown"
  try:
    sensor_type = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[6]/td[2]').get_attribute("textContent")
    sensor_type_strip=sensor_type.strip()
  except:
    sensor_type_strip = "unknown"
  try:
    crop_factor = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[9]/td[2]').get_attribute("textContent")
    crop_factor_strip=crop_factor.strip()
  except:
    crop_factor_strip = "unknown"
  try:
    optical_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[10]/td[2]').get_attribute("textContent")
    optical_zoom_strip=optical_zoom.strip()
  except:
    optical_zoom_strip = "unknown"
  try:
    digital_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[11]/td[2]').get_attribute("textContent")
    digital_zoom_strip=digital_zoom.strip()
  except:
    digital_zoom_strip = "unknown"
  try:
    iso = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[12]/td[2]').get_attribute("textContent")
    iso_strip=iso.strip()
  except:
    iso_strip = "unknown"
  try:
    raw = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[13]/td[2]').get_attribute('class')
    raw_strip=raw.strip()
  except:
    raw_strip = "unknown"
  try:
    manual_focus = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[14]/td[2]/span').get_attribute('class')
    manual_focus_strip=manual_focus.strip()
  except:
    manual_focus_strip = "unknown"
  try:
    focus_range = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[15]/td[2]').get_attribute("textContent")
    focus_range_strip=focus_range.strip()
  except:
    focus_range_strip = "unknown"
  try:
    focal_length = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[17]/td[2]').get_attribute("textContent")
    focal_length_strip=focal_length.strip()
  except:
    focal_length_strip = "unknown"
  try:
    aperture_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[18]/td[2]').get_attribute("textContent")
    aperture_priority_strip=aperture_priority.strip()
  except:
    aperture_priority_strip = "unknown"
  try:
    max_aperture = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[19]/td[2]').get_attribute("textContent")
    max_aperture_strip=max_aperture.strip()
  except:
    max_aperture_strip = "unknown"
  try:
    metering = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[22]/td[2]').get_attribute("textContent")
    metering_strip=metering.strip()
  except:
    metering_strip = "unknown"
  try:
    exposure_comp = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[23]/td[2]').get_attribute("textContent")
    exposure_comp_strip=exposure_comp.strip()
  except:
    exposure_comp_strip = "unknown"
  try:
    shutter_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[24]/td[2]').get_attribute("textContent")
    shutter_priority_strip=shutter_priority.strip()
  except:
    shutter_priority_strip = "unknown"
  try:
    min_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[25]/td[2]').get_attribute("textContent")
    min_ss_strip=min_ss.strip()
  except:
    min_ss_strip = "unknown"
  try:
    max_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[26]/td[2]').get_attribute("textContent")
    max_ss_strip=max_ss.strip()
  except:
    max_ss_strip = "unknown"
  try:
    built_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[27]/td[2]/span').get_attribute('class')
    built_flash_strip=built_flash
  except:
    built_flash_strip = "unknown"
  try:
    external_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[28]/td[2]/span').get_attribute("textContent")
    external_flash_strip=external_flash.strip()
  except:
    external_flash_strip = "unknown"
  try:
    viewfinder = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[29]/td[2]').get_attribute("textContent")
    viewfinder_strip=viewfinder.strip()
  except:
    viewfinder_strip = "unknown"
  try:
    whitebalance = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[30]/td[2]').get_attribute("textContent")
    whitebalance_strip=whitebalance.strip()
  except:
    whitebalance_strip = "unknown"
  try:
    screen_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[31]/td[2]').get_attribute("textContent")
    screen_size_strip=screen_size.strip()
  except:
    screen_size_strip = "unknown"
  try:
    screen_res = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[32]/td[2]').get_attribute("textContent")
    screen_res_strip=screen_res.strip()
  except:
    screen_res_strip = "unknown"
  try:
    video = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[33]/td[2]/span').get_attribute('class')
    video_strip=video
  except:
    video_strip = "unknown"
  try:
    storage = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[35]/td[2]').get_attribute("textContent")
    storage_strip=storage.strip()
  except:
    storage_strip = "unknown"
  try:
    battery = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[40]/td[2]').get_attribute("textContent")
    battery_strip=battery.strip()
  except:
    battery_strip = "unknown"
  try:
    weight = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[41]/td[2]').get_attribute("textContent")
    weight_strip=weight.strip()
  except:
    weight_strip = "unknown"
  try:
    dimensions = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[42]/td[2]').get_attribute("textContent")
    dimensions_strip=dimensions.strip()
  except:
    dimensions_strip = "unknown"
  try:
    year = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[43]/td[2]').get_attribute("textContent")
    year_strip=year.strip()
  except:
    year_strip = "unknown"

  query = """INSERT INTO cameras (`brand`,`model`,`megapixels`,`sensor_size`,`sensor_type`,`crop_factor`,`optical_zoom`,`digital_zoom`,`iso`,
  `raw`,`manual_focus`,`focus_range`,`focal_length`,`aperture_priority`,`max_aperature`,`metering`,`exposure_comp`,`shutter_priority`,
  `min_ss`,`max_ss`,`built_flash`,`external_flash`,`viewfinder`,`whitebalance`,`screen_size`,`screen_res`,`video`,`storage`,
  `battery`,`weight`,`dimension`,`year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
  mycursor.execute(query, (brand_strip, camera_model_strip, megapixels_strip, sensor_size_strip, sensor_type_strip, crop_factor_strip, optical_zoom_strip, digital_zoom_strip, iso_strip, raw_strip, manual_focus_strip, focus_range_strip, focal_length_strip, aperture_priority_strip, max_aperture_strip, metering_strip, exposure_comp_strip, shutter_priority_strip, min_ss_strip, max_ss_strip, built_flash_strip, external_flash_strip, viewfinder_strip, whitebalance_strip, screen_size_strip, screen_res_strip, video_strip, storage_strip, battery_strip, weight_strip, dimensions_strip, year_strip))
  mydb.commit()
  print('record added for' + camera_model_strip)

def regular():
  try:
    brand = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[1]/td[2]/a').get_attribute("textContent")
    brand_strip=brand.strip()
  except:
    brand_strip = "unknown"
  try:
    camera_model = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[2]/td[2]').get_attribute("textContent")
    camera_model_strip=camera_model.strip()
  except:
    camera_model_strip = "unknown"
  try:
    megapixels = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[4]/td[2]').get_attribute("textContent")
    megapixels_strip=megapixels.strip()
  except:
    megapixels_strip = "unknown"
  try:
    sensor_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
    sensor_size_strip=sensor_size.strip()
  except:
    sensor_size_strip = "unknown"
  try:
    sensor_type = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[6]/td[2]').get_attribute("textContent")
    sensor_type_strip=sensor_type.strip()
  except:
    sensor_type_strip = "unknown"
  try:
    crop_factor = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[9]/td[2]').get_attribute("textContent")
    crop_factor_strip=crop_factor.strip()
  except:
    crop_factor_strip = "unknown"
  try:
    optical_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[10]/td[2]').get_attribute("textContent")
    optical_zoom_strip=optical_zoom.strip()
  except:
    optical_zoom_strip = "unknown"
  try:
    digital_zoom = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[11]/td[2]').get_attribute("textContent")
    digital_zoom_strip=digital_zoom.strip()
  except:
    digital_zoom_strip = "unknown"
  try:
    iso = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[12]/td[2]').get_attribute("textContent")
    iso_strip=iso.strip()
  except:
    iso_strip = "unknown"
  try:
    raw = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[13]/td[2]').get_attribute('class')
    raw_strip=raw.strip()
  except:
    raw_strip = "unknown"
  try:
    manual_focus = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[14]/td[2]/span').get_attribute('class')
    manual_focus_strip=manual_focus.strip()
  except:
    manual_focus_strip = "unknown"
  try:
    focus_range = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[15]/td[2]').get_attribute("textContent")
    focus_range_strip=focus_range.strip()
  except:
    focus_range_strip = "unknown"
  try:
    focal_length = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[17]/td[2]').get_attribute("textContent")
    focal_length_strip=focal_length.strip()
  except:
    focal_length_strip = "unknown"
  try:
    aperture_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[18]/td[2]').get_attribute("textContent")
    aperture_priority_strip=aperture_priority.strip()
  except:
    aperture_priority_strip = "unknown"
  try:
    max_aperture = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[19]/td[2]').get_attribute("textContent")
    max_aperture_strip=max_aperture.strip()
  except:
    max_aperture_strip = "unknown"
  try:
    metering = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[21]/td[2]').get_attribute("textContent")
    metering_strip=metering.strip()
  except:
    metering_strip = "unknown"
  try:
    exposure_comp = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[22]/td[2]').get_attribute("textContent")
    exposure_comp_strip=exposure_comp.strip()
  except:
    exposure_comp_strip = "unknown"
  try:
    shutter_priority = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[23]/td[2]').get_attribute("textContent")
    shutter_priority_strip=shutter_priority.strip()
  except:
    shutter_priority_strip = "unknown"
  try:
    min_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[24]/td[2]').get_attribute("textContent")
    min_ss_strip=min_ss.strip()
  except:
    min_ss_strip = "unknown"
  try:
    max_ss = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[25]/td[2]').get_attribute("textContent")
    max_ss_strip=max_ss.strip()
  except:
    max_ss_strip = "unknown"
  try:
    built_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[26]/td[2]/span').get_attribute('class')
    built_flash_strip=built_flash
  except:
    built_flash_strip = "unknown"
  try:
    external_flash = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[27]/td[2]/span').get_attribute("textContent")
    external_flash_strip=external_flash.strip()
  except:
    external_flash_strip = "unknown"
  try:
    viewfinder = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[28]/td[2]').get_attribute("textContent")
    viewfinder_strip=viewfinder.strip()
  except:
    viewfinder_strip = "unknown"
  try:
    whitebalance = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[29]/td[2]').get_attribute("textContent")
    whitebalance_strip=whitebalance.strip()
  except:
    whitebalance_strip = "unknown"
  try:
    screen_size = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[30]/td[2]').get_attribute("textContent")
    screen_size_strip=screen_size.strip()
  except:
    screen_size_strip = "unknown"
  try:
    screen_res = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[31]/td[2]').get_attribute("textContent")
    screen_res_strip=screen_res.strip()
  except:
    screen_res_strip = "unknown"
  try:
    video = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[32]/td[2]/span').get_attribute('class')
    video_strip=video
  except:
    video_strip = "unknown"
  try:
    storage = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[34]/td[2]').get_attribute("textContent")
    storage_strip=storage.strip()
  except:
    storage_strip = "unknown"
  try:
    battery = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[39]/td[2]').get_attribute("textContent")
    battery_strip=battery.strip()
  except:
    battery_strip = "unknown"
  try:
    weight = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[40]/td[2]').get_attribute("textContent")
    weight_strip=weight.strip()
  except:
    weight_strip = "unknown"
  try:
    dimensions = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[41]/td[2]').get_attribute("textContent")
    dimensions_strip=dimensions.strip()
  except:
    dimensions_strip = "unknown"
  try:
    year = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[42]/td[2]').get_attribute("textContent")
    year_strip=year.strip()
  except:
    year_strip = "unknown"

  query = """INSERT INTO cameras (`brand`,`model`,`megapixels`,`sensor_size`,`sensor_type`,`crop_factor`,`optical_zoom`,`digital_zoom`,`iso`,
  `raw`,`manual_focus`,`focus_range`,`focal_length`,`aperture_priority`,`max_aperature`,`metering`,`exposure_comp`,`shutter_priority`,
  `min_ss`,`max_ss`,`built_flash`,`external_flash`,`viewfinder`,`whitebalance`,`screen_size`,`screen_res`,`video`,`storage`,
  `battery`,`weight`,`dimension`,`year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
  mycursor.execute(query, (brand_strip, camera_model_strip, megapixels_strip, sensor_size_strip, sensor_type_strip, crop_factor_strip, optical_zoom_strip, digital_zoom_strip, iso_strip, raw_strip, manual_focus_strip, focus_range_strip, focal_length_strip, aperture_priority_strip, max_aperture_strip, metering_strip, exposure_comp_strip, shutter_priority_strip, min_ss_strip, max_ss_strip, built_flash_strip, external_flash_strip, viewfinder_strip, whitebalance_strip, screen_size_strip, screen_res_strip, video_strip, storage_strip, battery_strip, weight_strip, dimensions_strip, year_strip))
  mydb.commit()
  print('record added for' + camera_model_strip)

for line in lisfile:
  #sparefile.write(line)
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Chrome('/Users/lukemitchell/chromedriver', chrome_options=options)
  websitelink = line.strip()
  driver.get(websitelink)
  print()
  time.sleep(0.4)
  thirdrow = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[3]/td[1]').get_attribute("textContent")
  thirdrow_strip = thirdrow.strip()
  camera = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[2]/td[2]').get_attribute("textContent")
  camera_strip = camera.strip()

  if thirdrow_strip == "Also known as:":
    dop = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[22]/td[1]').get_attribute("textContent")
    dop_strip = dop.strip()
    if dop_strip == "Depth of field:":
      print(camera_strip, " is a known as dop")
      knownas_dop()
    else:
      print(camera_strip, " is a known as")
      knownas()
  else:
    dop = driver.find_element_by_xpath('//*[@id="main"]/div[12]/table/tbody/tr[21]/td[1]').get_attribute("textContent")
    dop_strip = dop.strip()
    if dop_strip == "Depth of field:":
      print(camera_strip, " is a regular dop")
      regular_dop()
    else:
      print(camera_strip, " is a regular")
      regular()


