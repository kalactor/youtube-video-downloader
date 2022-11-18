from pytube import YouTube
import os
import subprocess

# this function download video in 1080p
def Download1080(url):
    try:
        yObj = YouTube(url)
        print(f"Downloading: {yObj.title}")
        vid = yObj.streams.filter(res="1080p").first().download()
        os.rename(vid, "video.mp4")
        aud = yObj.streams.filter(only_audio=True, abr="160kbps")
        aud = aud[0].download()
        os.rename(aud,"audio.webm")
        subprocess.call("./convert.sh")
        os.remove("video.mp4")
        os.remove("audio.webm")
    except:
        ("Check URL : error in downloading 1080p")

# this function download video in 720p
def DownloadOther(url):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        yt.streams.get_highest_resolution().download()
    except:
        print("Check URL: error in downloading 720p")


# main function logic
def Chooser():
    url = input("\nPlease enter youtube video url: ")
    print(f"Entered URL: {url}\n")
    print("Choose resolution: ")
    print("1. 1080p\n2. 720p\n")
    numberEntered = InputTaker()
    if numberEntered == 1:
        Download1080(url)
    elif numberEntered == 2:
        DownloadOther(url)
    else:
        print("Error")        


# taking user input for resolution
def InputTaker():
    num = 1
    while True:
        try:
            num = int(input("Choose 1 or 2 and [ctrl + c] to cancel: "))
            break
        except ValueError:
            print("Please enter a number.")
    return num


Chooser()
