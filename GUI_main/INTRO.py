from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("800x600")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("cool.gif")#enter the gif address 
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("music.mp3")#enter the music file address
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()