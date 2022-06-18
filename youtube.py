from pytube import YouTube
link = "https://www.youtube.com/watch?v=EAYlckSaviI"
video  = YouTube(link)
strms = video.streams.all()
# strms_audio = video.streams.filter(only_audio=True)
strms_audio = video.streams.get_audio_only()
strms_index = list(enumerate(strms))
print(strms_audio)
# for i in strms_audio:
#     print(i)

# strms[0].download()