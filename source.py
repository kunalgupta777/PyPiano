# Making a piano in Python! and Pygame!
# to fix:- make separate sound channels for each key, so that they can be played simultaneously, and add more piano sounds
# also, improve the UI a bit and if possible, structure the code in classes so that, it's easier to add or subtract new features
# from it.

import pygame as pg
import os
import math
import ctypes,time
import random
ctypes.windll.user32.SetProcessDPIAware()   # This fixes the high scaling DPI problem for Windows :)


# some colors

red     = (255,0,0)
green   = (0,255,0)
blue    = (0,0,255)
black   = (0,0,0)
white   = (255,255,255)
cyan    = (0,255,255)
magenta = (255,0,255)
yellow  = (255,255,0)



# centering the opened window

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.mixer.pre_init(44100, -16, 2, 2048)
pg.init()
font = pg.font.SysFont('Calibri',40)
title = font.render("PyPiano",True, red)
inst = font.render("Instructions:- Press the keyboard keys to play a key. Enjoy! :)",True,blue)
res = (1600,900)  # window size

sc = pg.display.set_mode(res)

pg.display.set_caption("PyPiano")

piano = pg.image.load('piano_image_2.png')
size = (int(1562/1.1),int(478/1.1))
piano = pg.transform.scale(piano,size)

clock = pg.time.Clock()
def disp(x):
    keyp = font.render(x,True,magenta)
    sc.blit(keyp,(730,800))

    
playok = False
pid = None
while True:
    if pid==None:
        pid=''
    for event in pg.event.get():
        if event.type==pg.QUIT:
            del font
            pg.quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_0:
                sound = pg.mixer.Sound("0.wav")
                sound.play()
                playok = True
                pid = '0'
            elif event.key==pg.K_1:
                sound = pg.mixer.Sound("1.wav")
                sound.play()
                playok = True
                pid = '1'
                
            elif event.key==pg.K_2:
                sound = pg.mixer.Sound("2.wav")
                sound.play()
                playok = True
                pid = '2'
            elif event.key==pg.K_3:
                sound = pg.mixer.Sound("3.wav")
                sound.play()
                playok = True
                pid = '3'
            elif event.key==pg.K_4:
                sound = pg.mixer.Sound("4.wav")
                sound.play()
                playok = True
                pid = '4'
            elif event.key==pg.K_5:
                sound = pg.mixer.Sound("5.wav")
                sound.play()
                playok = True
                pid = '5'
            elif event.key==pg.K_6:
                sound = pg.mixer.Sound("6.wav")
                sound.play()
                playok = True
                pid = '6'
            elif event.key==pg.K_7:
                sound = pg.mixer.Sound("7.wav")
                sound.play()
                playok = True
                pid = '7'
            elif event.key==pg.K_8:
                sound = pg.mixer.Sound("8.wav")
                sound.play()
                playok = True
                pid = '8'
            elif event.key==pg.K_9:
                sound = pg.mixer.Sound("9.wav")
                sound.play()
                playok = True
                pid = '9'
            elif event.key==pg.K_q:
                sound = pg.mixer.Sound("b1.wav")
                sound.play()
                playok = True
                pid = 'q'
            elif event.key==pg.K_w:
                sound = pg.mixer.Sound("b2.wav")
                sound.play()
                playok = True
                pid = 'w'
            elif event.key==pg.K_e:
                sound = pg.mixer.Sound("b3.wav")
                sound.play()
                playok = True
                pid = 'e'
            elif event.key==pg.K_r:
                sound = pg.mixer.Sound("b4.wav")
                sound.play()
                playok = True
                pid = 'r'
            elif event.key==pg.K_t:
                sound = pg.mixer.Sound("b5.wav")
                sound.play()
                playok = True
                pid = 't'
            elif event.key==pg.K_y:
                sound = pg.mixer.Sound("b6.wav")
                sound.play()
                playok = True
                pid = 'y'
            elif event.key==pg.K_u:
                sound = pg.mixer.Sound("b7.wav")
                sound.play()
                playok = True
                pid = 'u'
            elif event.key==pg.K_i:
                sound = pg.mixer.Sound("b8.wav")
                sound.play()
                playok = True
                pid = 'i'
            else:
                playok = False
    sc.fill(white)
    sc.blit(piano,(100,250))
    sc.blit(title,(740,60))
    sc.blit(inst,(420,120))
    if playok==True:
        disp(pid)
    
    pg.display.flip()
    
    clock.tick(60)  # 60 fps
    

