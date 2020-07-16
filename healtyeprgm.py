import time
import datetime
import pygame

def stopmusic():
    pygame.mixer.music.stop()

def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    # clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")

# from datetime import timedelta
currenttime=datetime.datetime.now()
print("Current time is ",currenttime)
time1=datetime.time(9,0,0)
maxtime=currenttime+datetime.timedelta(seconds=300)
print(type(maxtime))
print(maxtime)
file='C:\\Users\\acer\\PycharmProjects\\Healthyprgmr\\eyes.mp3'
while(currenttime<=maxtime):
    print("Currenttime",currenttime)
    print("Maxtime",maxtime)
    time.sleep(3)
    print("After 3second")
    try:
        pygame.mixer.init()
        file = 'C:\\Users\\acer\\PycharmProjects\\Healthyprgmr\\eyes.mp3'
        pmusic(file)
    except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
        stopmusic()
        print("\nPlay Stopped by user")
    except Exception:
        print("unknown error")

    time.sleep(10)
    try:
        pygame.mixer.init()
        file = 'C:\\Users\\acer\\PycharmProjects\\Healthyprgmr\\water.mp3'
        pmusic(file)
    except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
        # stopmusic()
        print("\nPlay Stopped by user")
    except Exception:
        print("unknown error")

    time.sleep(15)
    try:
        pygame.mixer.init()
        file = 'C:\\Users\\acer\\PycharmProjects\\Healthyprgmr\\exercise.mp3'
        pmusic(file)
    except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
        pygame.mixer.music.stop()
        # pygame.mixer.music.stop()
        # stopmusic()
        print("\nPlay Stopped by user")
    except Exception:
        print("unknown error")

    currenttime=datetime.datetime.now()
print("Time Up")
