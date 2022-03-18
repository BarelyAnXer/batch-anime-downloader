Find all urls in string
import re

def find_urls(s):
    return re.findall(r'(https?://\S+)', s)

find_urls('Visit this website https://recycledrobot.com')
