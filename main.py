from tkinter import Tk, filedialog
import eel
import requests
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

eel.init('web')

# 3 types of url
# base url = https://4anime.to/anime/kimetsu-no-yaiba
# episode url = https://4anime.to/kimetsu-no-yaiba-episode-01?id=16651
# video url = https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba
# -Episode-01-1080p.mp4

# download info structure {"title": "title1", "episode": "episode1", "size": "size1"}
download_info = []

# episodeUrls = [] if need every url ng bawat episode di yung vid
videoUrls = []
path = ""

isLoadingEps = False


@eel.expose
def getIsLoadingEps():
    return isLoadingEps


@eel.expose
def getAnimeInfo():
    return download_info


@eel.expose
def isPathValid(path):
    return os.path.isdir(path)


@eel.expose
def resetDownloadInfo():
    global download_info
    download_info = []


@eel.expose
def resetVideoUrls():
    global videoUrls
    videoUrls = []


def replace_all(text, dict):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text


@eel.expose
def download():
    global path
    invalid_Strings = {"<": "", ">": "", ":": "", "|": "", "?": "", "*": "", "/": "", "\\": "", "\"": ""}

    path = eel.getDirectory()()
    print("VIDEO URL", videoUrls)
    # TODO yung sa url ang problema 
    for index, value in enumerate(videoUrls):
        response = requests.get(value, stream=True)

        total_length = int(response.headers.get('content-length'))
        sizeDownloaded = 0

        print('downloading')

        title = download_info[index]["title"]
        episode = download_info[index]["episode"]

        # i imported pathlib for this so i the user can either use the browse button or
        # copy paste the directory pathlib.Path changes the path to a valid one so coppied path is ok not not just from
        # browse button for full name replace all invalid characters for naming a file  with ""
        fullname = replace_all(f"{title} {episode}.mp4", invalid_Strings)
        fullpath = os.path.join(Path(path), fullname)
        with open(fullpath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 256):
                f.write(chunk)
                sizeDownloaded = sizeDownloaded + len(chunk)
                progress = str(int((sizeDownloaded / total_length) * 100))
                if index == (len(videoUrls) - 1) and progress == "100":
                    yield progress
                    break
                yield progress
        print("done")
    print("downlaods done")


@eel.expose
def getDownloadProgress(value=download()):
    try:
        while True:
            return next(value)
    except StopIteration:
        pass
    # return next(value)


@eel.expose
def getDirectory():
    global path
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    dir_path = filedialog.askdirectory(initialdir="/", title="Select Location", parent=root)
    path = dir_path
    root.destroy()
    return dir_path


# this function will take the base url of the anime and get its info
# info like the title,episode,size
# example of base url
# https://4anime.to/anime/kimetsu-no-yaiba look at the top for more info
@eel.expose
def loadAnimeInfo(url):
    global isLoadingEps

    browser = webdriver.Chrome()
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#servers > div > div > ul')))
        print(element)
    except TimeoutException:
        print("server took too long to respond 1")
        browser.quit()
        loadAnimeInfo(url)

    try:
        soup = BeautifulSoup(browser.page_source, "html.parser")
        soup = soup.find_all("ul", class_="episodes range active")[0]
    except IndexError:
        print("index error")
        download()

    for i in soup.find_all("li"):
        # episodeUrls.append(i.a["href"]) if need every url ng bawat episode di yung vid
        browser.get(i.a["href"])
        try:
            WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, "#waytohideepisodes > ul")))
        #     ginamit ko tong selector nato kesa sa selector ng mistmong download button kasi
        # nag iiba iba selector ng dl depende sa episode
        except TimeoutException:
            print("server took too long to respond 2")

        soup = BeautifulSoup(browser.page_source, "html.parser")

        title = soup.find("a", {"id": "titleleft"}).text
        episode = soup.find("span", {"id": "titleleft"}).text
        videoUrl = soup.find("a", class_="mirror_dl")["href"]

        videoUrls.append(videoUrl)  # dito nakalagay yung mga video url para sa dl para mamaya

        response = requests.get(videoUrl, stream=True)
        total_length = int(int(response.headers.get('content-length')) / 1000) / 1000
        # converted to bytes converted to mb
        download_info.append({"title": title, "episode": episode, "size": total_length})

    isLoadingEps = True
    browser.quit()


eel.start('main.html', block=False)
# if block is true gagana lang yung code sa baba after i exit yung browser
# if block is false gagana kagad yung code sa baba kahit di i exit browser


while True:
    eel.sleep(1.0)
