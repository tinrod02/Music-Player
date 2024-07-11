from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from pygame import mixer

# Colors
co1 = "#FBEED7"
co2 = "#D9C19D"
co3 = "#B7966B"
co4 = "#946D43"
co5 = "#724A24"
co6 = "#502B0F"
co7 = "#2E1402"

# Initialize root window
root = Tk()
root.title("Music Player")
root.geometry("450x330")
root.configure(bg=co1)
root.resizable(width=FALSE, height=FALSE)

# Frames
leftframe = Frame(root, width=195, height=190, bg=co1)
leftframe.grid(row=0, column=0, padx=1, pady=1)

rightframe = Frame(root, width=260, height=190, bg=co6)
rightframe.grid(row=0, column=1, padx=0)

downframe = Frame(root, width=450, height=120, bg=co3)
downframe.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

# Listbox and Scrollbar
l_box = Listbox(rightframe, selectmode=SINGLE, font=("Arial 9 bold"), width=30, bg=co6, fg=co1)
l_box.grid(row=0, column=0)

loh = Scrollbar(rightframe)
loh.grid(row=0, column=1)

l_box.config(yscrollcommand=loh.set)
loh.config(command=l_box.yview)

# Function to load and resize images
def load_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)

# Images
music_image = load_image('icons/music.png', (130, 130))
app_img = Label(leftframe, height=130, image=music_image, padx=10, bg=co1)
app_img.place(x=30, y=40)

prev_image = load_image('icons/prev.png', (40, 40))
prev_btn = Button(downframe, height=40, image=prev_image, padx=1, bg='#C2AB8B', command=lambda: music_prev())
prev_btn.place(x=75, y=35)

play_image = load_image('icons/play.png', (40, 40))
play_btn = Button(downframe, height=40, image=play_image, padx=1, bg='#C2AB8B', command=lambda: music_play())
play_btn.place(x=125, y=35)

next_image = load_image('icons/fastf.png', (40, 40))
next_btn = Button(downframe, height=40, image=next_image, padx=1, bg='#C2AB8B', command=lambda: music_next())
next_btn.place(x=175, y=35)

pause_image = load_image('icons/pause.png', (40, 40))
pause_btn = Button(downframe, height=40, image=pause_image, padx=1, bg='#C2AB8B', command=lambda: music_pause())
pause_btn.place(x=225, y=35)

con_image = load_image('icons/con.png', (40, 30))
con_btn = Button(downframe, height=40, image=con_image, padx=1, bg='#C2AB8B', command=lambda: music_con())
con_btn.place(x=275, y=35)

stop_image = load_image('icons/stop.png', (40, 40))
stop_btn = Button(downframe, height=40, image=stop_image, padx=1, bg='#C2AB8B', command=lambda: music_stop())
stop_btn.place(x=325, y=35)

# Lines
line = Label(leftframe, width=200, height=1, padx=10, bg=co6)
line.place(x=0, y=1)
line = Label(leftframe, width=200, height=1, padx=10, bg=co1)
line.place(x=0, y=5)

# Song Label
song = Label(downframe, width=70, text="Select a Song", font=("Arial 10"), height=1, bg=co1, fg="black", anchor=NW)
song.place(x=0, y=1)

# Actions
def music_play():
    run = l_box.get(ACTIVE)
    song['text'] = run
    mixer.music.load(run)
    mixer.music.play()

def music_pause():
    mixer.music.pause()

def music_con():
    mixer.music.unpause()

def music_stop():
    mixer.music.stop()

def music_next():
    plays = song['text']
    index = songs.index(plays)
    new_index = index + 1 if index + 1 < len(songs) else 0
    plays = songs[new_index]
    mixer.music.load(plays)
    mixer.music.play()

    l_box.delete(0, END)
    show()
    l_box.select_set(new_index)
    song['text'] = plays

def music_prev():
    plays = song['text']
    index = songs.index(plays)
    new_index = index - 1 if index > 0 else len(songs) - 1
    plays = songs[new_index]
    mixer.music.load(plays)
    mixer.music.play()

    l_box.delete(0, END)
    show()
    l_box.select_set(new_index)
    song['text'] = plays

# File dialog to select music folder
def select_music_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        os.chdir(folder_selected)
        global songs
        songs = os.listdir()
        show()

# Set the music directory
select_music_folder()

# Function to display songs in the listbox
def show():
    l_box.delete(0, END)
    for i in songs:
        l_box.insert(END, i)

# Initialize mixer
mixer.init()
music_state = StringVar()
music_state.set("Choose One!")

# Start the GUI loop
root.mainloop()
