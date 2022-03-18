import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome(r"C:\Users\63966\Desktop\chrome driver\chromedriver.exe")
browser.get("https://4anime.to/anime/nekopara")


eps = []

time.sleep(10)  # to load the page beacasue of cloudfare
soup = BeautifulSoup(browser.page_source, "html.parser")
soup = soup.find_all("ul", class_="episodes range active")[0]

print(eps)

for i in soup.find_all("li"):
    eps.append(i.a["href"])
    print(i.a["href"])
    browser.get(i.a["href"])
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # get the name and what episode and the download link videourl
    animeTitle = soup.find("a", {"id": "titleleft"}).text
    animeEpisode = soup.find("span", {"id": "titleleft"}).text
    videoURL = soup.find("a", class_="mirror_dl")["href"]

    print(f"{animeTitle} {animeEpisode} {videoURL}")

    response = requests.get(videoURL, stream=True)
    total_length = int(response.headers.get('content-length'))
    print(f"downloading {total_length} bytes of data")

    # with open("C:/Users/63966/Desktop/New folder/" + f"{animeTitle} {animeEpisode}.mp4", "wb") as f:
    #     sizeDownloaded = 0
    #     for chunk in response.iter_content(chunk_size=1024*256):
    #         f.write(chunk)
    #         sizeDownloaded = sizeDownloaded + len(chunk)
    #         final = str(int((sizeDownloaded / total_length) * 100))
    #         if final == "100":
    #             final = "Completed"
    #         # print(final)
    #
    # print("done")

time.sleep(5)
browser.quit()
print(eps)
