from tkinter import filedialog
from tkinter import *
import music

config = {
    "fileType": ".mp3",
    "tempo":120,
    "key":"C Major",
    "Instrument":{
        "id":0,
        "name":"Piano",
        "path":""
    },
    "channel_amount":8,
    "Drum":{
        "id":1,
        "name":"Drum",
        "path":"Audio.Drumkit/"
    }
}
root = Tk()


Queue = []
def picksong():

    songdir = filedialog.askopenfilename(title='Pick song',initialdir='/',filetypes=(('Audio','*.mp3'),('All Files','*.*')))

    songdir = songdir.replace('/','\\').removesuffix('.mp3')
    Queue.append(songdir)

def playsong(dir):
    music.play(0,dir,duration=15000000,configuration=config)
    music.wait()

masterinput = input("Select Option (Pick Song, Play Song)>")

pos = 0
while pos < len(Queue):
    if masterinput.lower() == "pick song":
        picksong()
    elif masterinput.lower() == "play song":
        playsong(Queue[pos])
    pos+=1