import requests
from bs4 import BeautifulSoup

url = "https://www.gogoanime1.com/watch/yahari-ore-no-seishun-love-come-wa-machigatteiru"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
soup = soup.findAll("ul", class_="check-list")[1]

for i, value in enumerate(soup.findAll("li"), 1):
    print(i, value.a["href"])

    # checking if the episode is first between or last
    # if first or last index is 1 because there is only next and download button that is why its [1]
    # else index is 2 because there is 3 previous next and download that is why its [2]
    if i == 1 or i == len(soup.findAll("li")):
        index = 1
    else:
        index = 2

    response = requests.get(value.a["href"]).text
    soup = BeautifulSoup(response, "html.parser")

    # getting the name and number of what episode it is
    name = soup.find("div", "vmn-title").h1.text

    # geeting the vid url
    temp = soup.find("div", class_="vmn-buttons")
    temp = temp.findAll("a")[index]["href"]

    print(temp)

    # download vid code
    print("downloading")
    try:
        r = requests.get(temp, stream=True)
    except Exception:
        print("exception")
        continue

    if r.ok:
        with open(name + ".mp4", "wb") as f:
            for chunk in r.iter_content(chunk_size=256):
                f.write(chunk)
    else:
        continue
    print("done")
