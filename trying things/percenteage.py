import requests

link = "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-01-1080p.mp4"
file_name = "download.mp4"
with open(file_name, "wb") as f:
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None:  # no content length header
        f.write(response.content)
    else:
        sizeDownloaded = 0
        total_length = int(total_length)
        temp = int((total_length/1000))
        for data in response.iter_content(chunk_size=1024 * 256):
            # print(len(data))
            f.write(data)
            sizeDownloaded = sizeDownloaded + len(data)
            final = str(int((sizeDownloaded / total_length) * 100))
            if final == "100":
                final = "Completed"
                print(final)
            print(f"\r{final}", end="")
