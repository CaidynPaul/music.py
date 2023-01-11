from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry("700x490")
Heading = Label(root, text="Welcome to music.py setup",font="Helvetic 24 bold")
Heading.pack()

musicdata = """import pygame
import json
import time
import os

os.chdir('Music')
#open config.json
config = open('config.json', 'r')
config_data = json.load(config)
pygame.mixer.init(buffer=2048,channels=config_data.get('channel_amount'))

def get_metadata():
    f = open('config.json','r')
    alldata = json.load(f)
    tempo_data = alldata.get('tempo')
    instrument_data = alldata['instrument']['name']
    channel_data = alldata.get('channel')
    f.close()

    output = '''
Tempo : {},
Default Instrument : {},
Number of Channels : {},

-----------------------------------------------------------------------------

Config Data: {}.
    '''.format(tempo_data, instrument_data, channel_data, alldata)
    return output

def play(layer:int,notes:str,duration:int=1000,configuration=config_data):
    global waitDuration
    waitDuration = duration
    pygame.mixer.Channel(layer).play(pygame.mixer.Sound(configuration['Instrument']['path']+notes.title()+configuration['fileType']),maxtime=duration)

def wait():
    time.sleep(waitDuration/1000)

def main():
    play(1,'C3')
    play(2,'E3')
    play(3,'G3')

if __name__ == '__main__':
    print('Playing C MAJOR Chord')
    main()
    # useless input to ensure the audio plays
    input('Press Enter to continue...')

while pygame.mixer.get_busy():
        pygame.time.delay(100)

# close config.json at end of module
# to be able to access data in config.json without opening
# and closing it repeatedly
# A.K.A being lazy
config.close()

print('Playing Song...')"""
configdata = '''{
    "fileType": ".mp3",
    "tempo":120,
    "key":"C Major",
    "Instrument":{
        "id":0,
        "name":"Piano",
        "path":"Audio.Piano/"
    },
    "channel_amount":8,
    "Drum":{
        "id":1,
        "name":"Drum",
        "path":"Audio.Drumkit/"
    }
}'''
ex1data = '''from music import *

# This will play the A Major Chord
play(0,'A3',1)
play(1,'Db4',1)
play(2,'E4',1)

wait()
'''
ex2data = '''import music
import json

new_config_file = open('fake.json','r')
new_config_data = json.load(new_config_file)

music.play(0,'<Insert Song Here>',1000,new_config_data)
music.wait()
'''
readmedata = '''## Dependencies
pygame module'''
initdata = ''


def setup():
    dir = filedialog.askdirectory()
    with open(f"{dir}/music.py",'w') as music:
        music.write(musicdata)
    with open(f"{dir}/config.json",'w') as config:
        config.write(configdata)
    with open(f"{dir}/example1.py",'w') as ex1:
        ex1.write(ex1data)
    with open(f"{dir}/example2.py",'w') as ex2:
        ex2.write(ex2data)
    with open(f"{dir}/README.md",'w') as readme:
        readme.write(readmedata)
    with open(f'{dir}/__init__.py','w') as init:
        init.write("")
    def close():
        root.destroy()
    start.config(text="Close",command=close)


start = Button(root, text="Start Setup",command=setup)
start.pack()


root.mainloop()