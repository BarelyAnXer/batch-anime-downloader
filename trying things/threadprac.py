import concurrent.futures
import time

import requests

x = [
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-01-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-02-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-03-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-04-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-05-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-06-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-07-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-08-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-09-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-10-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-11-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-12-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-13-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-14-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-15-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-16-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-17-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-18-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-19-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-20-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-21-1080p.mp4",
    'https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-22-1080p.mp4',
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-23-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-24-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-25-1080p.mp4",
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-26-1080p.mp4"]


def dl(index):
    r = requests.get(x[index], stream=True)

    total_length = r.headers.get('content-length')
    sizeDownloaded = 0
    total_length = int(total_length)

    with open(f"dl{index}" + ".mp4", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
            # sizeDownloaded = sizeDownloaded + len(chunk)
            # final = str(int((sizeDownloaded / total_length) * 100))
            # if final == "100":
            #     final = "Completed"
            # print(f"\r{final}", end="")
    print(f"done {index}")


def dlurl(url):
    r = requests.get(url, stream=True)
    ctr = 0
    print(f"downloading {ctr}")
    with open(f"dl{ctr}" + ".mp4", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 256):
            f.write(chunk)
        ctr = ctr + 1
    print(f"done {ctr}")


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(dlurl, x)
    print(time.perf_counter())


if __name__ == '__main__':
    main()
