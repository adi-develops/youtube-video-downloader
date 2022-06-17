from pytube import YouTube
link = "https://www.youtube.com/watch?v=EAYlckSaviI"
video  = YouTube(link)
strms = video.streams.all()
strms_audio = video.streams.filter(only_audio=True)
strms_index = list(enumerate(strms))
# for i in strms_index:
#     print(i)

strms[0].download()