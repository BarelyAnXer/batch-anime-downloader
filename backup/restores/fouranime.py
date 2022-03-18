import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


# options = webdriver.ChromeOptions()
# options.headless = True
browser = webdriver.Chrome()#,options=options)
# di gumagana pag nag headls ako ?? why
browser.set_window_position(-10000, 0)


class FourAnimeScraper:

    def __init__(self, url):
        # url , episodes to download ex 1,2,3-5 parse muna gamit regex then tingin sa array ng mga ep
        # path
        self.url = url

    def getEpisodes(self):
        episodes = []
        browser.get(self.url)
        time.sleep(15)  # to load the page beacasue of cloudfare
        soup = BeautifulSoup(browser.page_source, "html.parser")
        soup = soup.find_all("ul", class_="episodes range active")[0]
        for i in soup.find_all("li"):
            episodes.append(i.a["href"])
        print(episodes)

        return episodes

    def getInfo(self, temp):
        new_list = list()
        for index, value in enumerate(temp, 1):
            browser.get(value)
            soup = BeautifulSoup(browser.page_source, "html.parser")

            animeTitle = soup.find("a", {"id": "titleleft"}).text
            animeEpisode = soup.find("span", {"id": "titleleft"}).text
            videoURL = soup.find("a", class_="mirror_dl")["href"]

            new_tuple = animeTitle, animeEpisode, videoURL
            new_list.append(new_tuple)

        return new_list

    def downloadVideo(self):
        info = self.getInfo(self.getEpisodes())
        # for indexI, valueI in enumerate(info):
        # for indexJ, valueJ in enumerate(valueI):
        #     print(indexI, valueI[indexJ])
        # 0 = animeTitle
        # 1 = animeEpisode
        # 2 = videoURL
        # 3 = response
        # 4 = total_length

        for i in info:
            response = requests.get(i[2], stream=True)
            total_length = int(response.headers.get('content-length'))
            print(response, total_length, "downloading")
            with open("C:/Users/63966/Desktop/New folder/" + f"{i[0]} {i[1]}.mp4", "wb") as f:
                sizeDownloaded = 0
                for chunk in response.iter_content(chunk_size=1024 * 256):
                    f.write(chunk)
                    sizeDownloaded = sizeDownloaded + len(chunk)
                    final = str(int((sizeDownloaded / total_length) * 100))
                    if final == "100":
                        final = "Completed"
                    # print(final)
            print("done")

        time.sleep(10)
        browser.quit()


def main():
    a = FourAnimeScraper("https://4anime.to/anime/toradora")
    a.downloadVideo()


if __name__ == '__main__':
    main()
