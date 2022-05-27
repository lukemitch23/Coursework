from bs4 import BeautifulSoup
import requests

page_url = "https://www.digicamdb.com/specs/nikon_z9/"

page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

file = open('website.txt', 'w')
file.write(str(soup))