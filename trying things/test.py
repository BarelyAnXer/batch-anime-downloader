import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = "https://4anime.to/nekopara?id=22644"
browser = webdriver.Chrome(r"C:\Users\63966\Desktop\chrome driver\chromedriver.exe")
browser.get(url)
time.sleep(6)

soup = BeautifulSoup(browser.page_source, "html.parser")
title = soup.find("a", {"id": "titleleft"}).text
episode = soup.find("span", {"id": "titleleft"}).text
videoURL = soup.find("a", class_="mirror_dl")["href"]

print(f"{title} {episode} {videoURL}")


browser.quit()
