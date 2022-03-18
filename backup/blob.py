import requests
import pprint
import m3u8



url = "https://fxmnz.mcloud.to/19fb7c5f969e6fff0/b87534173b6948a11207bb0dc7b6ea8782eb10594b08879feea606b51f51ee34ee07f7ee2350f6fafacd2736ac68b413e3e9c2f4f8b621e4e58732a22e90719e7c85a98b9424c413bea409d18954297988edf650570573db1cc0fa1d11fae977/list.m3u8"

url = "https://9anime.to/watch/is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-ii-dub.qo2w/q5qn95"

response = requests.get(url, stream = True)

print(response.content)