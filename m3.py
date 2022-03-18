import requests

headers = {
"authority": "cmgar.mcloud.to",
"method": "GET",
"path": "/2001b4a46f4a002bd593/d829c8a01d02d740af992c743d645e4ee60307960be1b4509f366c3ddf952b3bd859b0aa19391adaf912c0220151825d2eab501f0dd161f505cb39021709f3e0938e18c66cb4bafd8c2cebd2de7b2c62d2af696ad70b9aae095a5a4a012e2532/list.m3u8",
"scheme": "https",
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "no-cache",
"origin": "https://mcloud.to",
"pragma": "no-cache",
"referer": "https://mcloud.to/embed/yjkk9x?key=77d7aeb199cd62b9978cc4272c2c8d4db3bdb60a601df4d59391f1f0512b8465&autostart=true",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

url = "https://cmgar.mcloud.to/2001b4a46f4a002bd593/d829c8a01d02d740af992c743d645e4ee60307960be1b4509f366c3ddf952b3bd859b0aa19391adaf912c0220151825d2eab501f0dd161f505cb39021709f3e0938e18c66cb4bafd8c2cebd2de7b2c62d2af696ad70b9aae095a5a4a012e2532/list.m3u8"

response = requests.get(url,headers = headers)

print(response)