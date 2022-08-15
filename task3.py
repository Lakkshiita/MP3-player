import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from PIL import ImageTk, Image


# functions

def open_folder():
    path = filedialog.askdirectory()
    os.chdir(path)
    songs = os.listdir(path)
    for s in songs:
        if'.mp3' in s:
             playlist.insert(END, s)
            # else:
            #     messagebox.showinfo('Wait!!', 'no audio files found')
            #     break


def play():
	# try:
		currentsong = playlist.get(ACTIVE)
		mixer.music.load(currentsong)
		mixer.music.play()
		# songstatus.set("Playing  "+currentsong)
	# except:
	# 	messagebox.showinfo('wait','select a directory')


def pause():
    try:
        mixer.music.pause()
        # songstatus.set("Paused")
    except:
        messagebox.showinfo('wait','select a directory')

def stop():
    try:
        mixer.music.stop()
        # songstatus.set("Stopped")
    except:
        messagebox.showinfo('wait','select a directory')


def resume():
    try:
        mixer.music.unpause()
        # songstatus.set("Resuming")
    except:
        messagebox.showinfo('wait','select a directory')


# tkinter window
main = Tk()
main.title('Music Player')
main['background'] = 'black'
main.geometry('800x600')
# pygame mixer to play music


mixer.init()
# songstatus = StringVar()  # this is us to display the current song status
# songstatus.set("Select Folder")



#Create an object of Scrollbar widget
s = Scrollbar()

#Create a horizontal scrollbar
scrollbar = Scrollbar(main, orient= 'vertical')
scrollbar.pack(side= RIGHT, fill= BOTH)


playlist = Listbox(main, selectmode=SINGLE, bg="grey",  width=100, height=10,  fg="white", font=('arial', 15))
# playlist.grid(columnspan=7)
playlist.pack()


playlist.config(yscrollcommand= scrollbar.set)

#Configure the scrollbar
scrollbar.config(command= playlist.yview)

# icon image
icon_image = PhotoImage(file='icon.png')
main.iconphoto(False,icon_image)


# resume img
resume_img = Image.open("resume.png")
resume_img_resize = resume_img.resize((60, 60))
resume_img_btn = ImageTk.PhotoImage(resume_img_resize)

# folder img
folder_img = Image.open("folder.png")
folder_img_resize = folder_img.resize((90, 90))
folder_img_resize_btn = ImageTk.PhotoImage(folder_img_resize)

# play img
play_img = Image.open("play.png")
play_img_resize = play_img.resize((60, 60))
play_img_resize_btn = ImageTk.PhotoImage(play_img_resize)

# pause img
pause_img = Image.open("pause.png")
pause_img_resize = pause_img.resize((60, 60))
pause_img_resize_btn = ImageTk.PhotoImage(pause_img_resize)

# stop img
stop_img = Image.open("stop.png")
stop_img_resize = stop_img.resize((60, 60))
stop_img_resize_btn = ImageTk.PhotoImage(stop_img_resize)

# pplay btn
playbtn = Button(main, text="play", image=play_img_resize_btn, borderwidth=0, command=play)
playbtn.config(font=('arial', 20), bg="#000000", fg="white",)
playbtn.place(x=500,y=400)

# folder btn
filebt = Button(main, text="file", image=folder_img_resize_btn,borderwidth=0, bg="#000000", command=open_folder)
filebt.config(font=('arial', 20),fg="white",)
filebt.place(x=345,y=310)

# pause btn
pausebtn = Button(main, text="Pause", image=pause_img_resize_btn, borderwidth=0, bg="#000000", command=pause)
pausebtn.config(font=('arial', 20),fg="white", padx=7, pady=7)
pausebtn.place(x=400,y=400)

# stop btn
stopbtn = Button(main, image=stop_img_resize_btn,borderwidth=0, bg="#000000", command=stop)
stopbtn.config(font=('arial', 20), fg="white", padx=7, pady=7)
stopbtn.place(x=300,y=400)

# resume btn
Resumebtn = Button(main, image=resume_img_btn, borderwidth=0, bg="#000000", command=resume)
Resumebtn.config(font=('arial', 20),fg="white", padx=7, pady=7)
Resumebtn.place(x=200,y=400)

# label = Label(main, textvariable=songstatus, relief=RAISED,
#               height=2, width=50,font=("Arial", 15), bg='#2b2928', fg='#ffffff')
# label.place(x=130,y=250)



main.mainloop()