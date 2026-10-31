#import pytube


import yt_dlp
url=input("Enter the URL you would like to download: ")
ydl_opts ={'format':'best[height<=720] ','outtmpl':'%(title)s.%(ext)s'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Download Completed")
