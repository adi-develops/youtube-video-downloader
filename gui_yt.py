from tkinter import *
from tkinter.filedialog import askdirectory
from pytube import YouTube
import shutil

def select_path():
    # Allows user to select a path from File Explorer
    path = askdirectory
    path_label.config(text = path)

def download_video():
    user_link = link_field.get()    # Get the link entered by the user
    user_path = path_label.cget("text")     # Get the path entered by the user from the label
    root.title("Downloading...")
    video = YouTube(user_link).streams.get_highest_resolution().download()   # Used to download the video
    root.title("Video Download Complete!")
    shutil.move(video, user_path)   # Used to move the video to the desired directory

def download_audio():
    user_link = link_field.get()
    user_path = path_label.cget("text")
    root.title("Downloading...")
    audio = YouTube(user_link).streams.get_audio_only().download()   # Used to download the audio
    root.title("Audio Download Complete!")
    shutil.move(audio, user_path)   # Used to move the video to the desired directory

root = Tk()
root.title("YouTube Video Downloader")
# root.geometry("500x600")
title = PhotoImage(file='title.png')
root.iconphoto(False, title)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

logo = PhotoImage(file='yt.png')
logo = logo.subsample(2,2)

canvas.create_image(250, 80, image=logo)

link_field = Entry(root, width=50)
link_label = Label(root, text="Enter Download Link: ", font = ('Arial', 15))

path_label = Label(root, text="Select Path for Download: ", font = ('Arial', 15))
select_btn = Button(root, font = ('Arial', 12), text="Select", command=select_path)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(root, font = ('Arial', 12), text="Download Video", command=download_video)
canvas.create_window(250, 390, window=download_btn)
audio_download_btn = Button(root, font = ('Arial', 12), text="Download Audio", command=download_audio)
canvas.create_window(250, 440, window=audio_download_btn)

root.mainloop()