from tkinter import *

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
select_btn = Button(root, text="Select")

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(root, text="Download File")
canvas.create_window(250, 390, window=download_btn)

root.mainloop()