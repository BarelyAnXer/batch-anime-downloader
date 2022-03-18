import concurrent.futures
import requests
import time


def download(index):
    r = requests.get(x[index], stream=True)

    with open(f"dl{index}" + ".mp4", "wb") as f:
        print(f"downloading... {index}")
        for chunk in r.iter_content(chunk_size=1024 * 256):
            f.write(chunk)

    print(f"done {index}")


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
    "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-10-1080p.mp4"]


# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-11-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-12-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-13-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-14-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-15-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-16-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-17-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-18-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-19-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-20-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-21-1080p.mp4",
# 'https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-22-1080p.mp4',
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-23-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-24-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-25-1080p.mp4",
# "https://storage.googleapis.com/linear-theater-254209.appspot.com/v2.4animu.me/Kimetsu-no-Yaiba/Kimetsu-no-Yaiba-Episode-26-1080p.mp4"]


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as cfp:
        for i in range(len(x)):
            cfp.submit(download, i)
    print(time.perf_counter())


# 646.5187857 process
# 631.6814304 threading
if __name__ == '__main__':
    main()
