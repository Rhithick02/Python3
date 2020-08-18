import pytube
url = input()
youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download('/home/rhithick/Downloads/')