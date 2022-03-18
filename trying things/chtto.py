import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

download_info = [
    {"title": "title1", "episode": "episode1", "size": "size1"}
]

# function without s and with s to determine if array ng url yung
# nagiisang argument or isant string lng na url

def getInfo(url):
    browser = webdriver.Chrome(r"C:\Users\63966\Desktop\chrome driver\chromedriver.exe")
    browser.get(url)

    try:
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "#waytohideepisodes > ul > li:nth-child(1) > a")))
    except TimeoutException:
        print("server took too long to respond")
    # finally:
    #     browser.quit()

    soup = BeautifulSoup(browser.page_source, "html.parser")
    title = soup.find("a", {"id": "titleleft"}).text
    episode = soup.find("span", {"id": "titleleft"}).text
    videoURL = soup.find("a", class_="mirror_dl")["href"]

    response = requests.get(videoURL, stream=True)
    total_length = int(response.headers.get('content-length'))

    download_info.append({"title": title, "episode": episode, "size": total_length})

    browser.get("https://4anime.to/kimetsu-no-yaiba-episode-02?id=17783")
    input("press enter to exit")


getInfo("https://4anime.to/kimetsu-no-yaiba-episode-01?id=16651")

for i in range(len(download_info)):
    print(i)

# def getInfo(url):
#     browser = webdriver.Chrome(r"C:\Users\63966\Desktop\chrome driver\chromedriver.exe")
#     browser.get(url)
#     eel.sleep(10)  # try mamaya time.sleep need to para hintayin mag laoad yung page
#     # i upate to gawing dynamic yung paghintay ng pag load
#
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     title = soup.find("a", {"id": "titleleft"}).text
#     episode = soup.find("span", {"id": "titleleft"}).text
#     videoURL = soup.find("a", class_="mirror_dl")["href"]
#
#     response = requests.get(videoURL, stream=True)
#     total_length = int(response.headers.get('content-length'))
#
#     download_info.append({"title": title, "episode": episode, "size": total_length})
#     browser.quit()