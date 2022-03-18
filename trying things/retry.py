from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def download(url):
    browser = webdriver.Chrome()
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#servers > div > div > ul')))
        print(element)
    except TimeoutException:
        print("server took too long to respond 1")
    try:
        soup = BeautifulSoup(browser.page_source, "html.parser")
        soup = soup.find_all("ul", class_="episodes range active")[0]
        print(soup)
    except IndexError:
        print("ey")
        download(url)


url = "https://4anime.to/anime/princess-connect-redive"
download(url)
