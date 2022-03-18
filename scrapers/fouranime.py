import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser = None


def Initialize():
    browser = webdriver.Chrome()
    return browser



class FourAnimeScraper:
    @staticmethod
    def Initialize():
        global Instance
        Instance = webdriver.Chrome("driver path")
        Instance.implicitly_wait(5)
        return Instance

    @staticmethod
    def CloseDriver():
        global Instance
        Instance.quit()

    def __init__(self, url):
        self.url = url
        self.download_info = []

    # def setUp(self):
    #     self.browser = webdriver.Firefox()
    #     self.addCleanup(self.browser.quit)
    #
    # def testPageTitle(self):
    #     self.browser.get('http://www.google.com')

    def getAnimeInfo(self):
        browser = Initialize()
        browser.get(self.url)

        try:
            WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, "#servers > div > div > ul")))
        except TimeoutException:
            print("server took too long to respond 1")

        soup = BeautifulSoup(browser.page_source, "html.parser")
        soup = soup.find_all("ul", class_="episodes range active")[0]

        for i in soup.find_all("li"):
            browser.get(i.a["href"])
            print(i.a["href"])
            try:
                WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#my_video > div.jw-media.jw-reset > video")))
            except TimeoutException:
                print("server took too long to respond 2")

            soup = BeautifulSoup(browser.page_source, "html.parser")

            title = soup.find("a", {"id": "titleleft"}).text
            episode = soup.find("span", {"id": "titleleft"}).text
            videoUrl = soup.find("a", class_="mirror_dl")["href"]

            response = requests.get(videoUrl)
            total_length = int(response.headers.get('content-length'))

            self.download_info.append({"title": title, "episode": episode, "size": total_length})
        browser.quit()


def main():
    scraper = FourAnimeScraper("https://4anime.to/anime/toradora")
    scraper.getAnimeInfo()
    print(scraper.download_info)


if __name__ == '__main__':
    main()
