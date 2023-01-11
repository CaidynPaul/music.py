import pygame
import json
import time
import os


#open config.json
config = open('config.json', 'r')
config_data = json.load(config)
pygame.mixer.init(buffer=2048,channels=config_data.get('channel_amount'))

def play(layer:int,notes:str,duration:int=1000,configuration=config_data):
    global waitDuration
    waitDuration = duration
    pygame.mixer.Channel(layer).play(pygame.mixer.Sound(configuration['Instrument']['path']+notes.title()+configuration['fileType']),maxtime=duration)

def wait():
    time.sleep(waitDuration/1000)

def save():
    pass


def main():
    play(1,'C3')
    play(2,'E3')
    play(3,'G3')

if __name__ == '__main__':
    print('Playing C MAJOR Chord')
    main()
    # useless input to ensure the audio plays
    input('Press Enter to continue...')

if os.getcwd().endswith('Music') != 'Music':
    os.chdir('../Music')

while pygame.mixer.get_busy():
        pygame.time.delay(100)

# close config.json at end of module
# to be able to access data in config.json without opening
# and closing it repeatedly
# A.K.A being lazy
config.close()

print('Playing Song...')