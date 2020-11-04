################################################################ 
#  ___ ___   ___    ___   ____   ______  __ __  ____     ___   #
# |   |   | /   \  /   \ |    \ |      ||  |  ||    \   /  _]  #
# | _   _ ||     ||     ||  _  ||      ||  |  ||  o  ) /  [_   #
# |  \_/  ||  O  ||  O  ||  |  ||_|  |_||  ~  ||   _/ |    _]  #
# |   |   ||     ||     ||  |  |  |  |  |___, ||  |   |   [_   #
# |   |   ||     ||     ||  |  |  |  |  |     ||  |   |     |  #
# |___|___| \___/  \___/ |__|__|  |__|  |____/ |__|   |_____|  #
#                                                              #
################################################################

################################################################
#                                                              #
# moontype.py
# -----------
#
# date:   november 2020
# author: Nicolas Méloni
#         Toulon, France
# source: https://github.com/nmeloni
#                                                              #
################################################################

################################################################
# 
# MOONTYPE is a typing shmup developed for the Github/itch.io
# game jam of november 2020 and a first attempt at game
# programming.
#
# Theme : MOONSHOT
# Pitch : The moon is collapsing and threatens the earth.
#         Use your more poetic instincts to type your way
#         through the meteors and save humanity !
################################################################

import pyxel
from random import randrange


MT_SCREEN_X = 256
MT_SCREEN_Y = 256

MT_PYXEL_KEY_OFFSET = pyxel.KEY_A 
MT_ASCII_KEY_OFFSET = ord("a")

POEME = ["la","nuit","je","mens","je","prends","des","trains","a","travers","la","pleine"]

class Meteor():
    """Falling meteor attached to a text"""
    def __init__(self, x,y,text):
        self.x = x
        self.y = y
        self.active = False
        self.text = text
        self.text_x = x+8 - len(text)*2
        self.text_y = y-8
        self.active_letter = 0
        self.hit_frame = 0

    def update(self):
        self.y+=1 #1 px fall
        self.hit_frame = max(0,self.hit_frame-1)
        
    def hit(self):
        self.active_letter += 1
        return self.active_letter == len(self.text)

class App():
    def __init__(self):
        pyxel.init(MT_SCREEN_X,MT_SCREEN_Y, caption="--- MOONTYPE --- ")
        pyxel.load("moontype.pyxres")


        self.poem = POEME[::-1]
        self.meteor_list = [Meteor(randrange(16,240),0,self.poem.pop())]
        self.meteor_list[0].active = True
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if (pyxel.frame_count % 30 == 0) and (len(self.poem)!=0):
            self.meteor_list.insert(0,Meteor(randrange(16,240),0,self.poem.pop()))
        for meteor in self.meteor_list:
            meteor.update()

        if len(self.meteor_list) != 0: 
            meteor = self.meteor_list[-1]
            letter = meteor.text[meteor.active_letter]
            if pyxel.btn( ord(letter)-MT_ASCII_KEY_OFFSET+MT_PYXEL_KEY_OFFSET ):
                if meteor.hit():
                    self.meteor_list.pop()
        
    def draw_meteor(self, meteor):
        i = meteor.active_letter
        pyxel.text(meteor.text_x, meteor.y-5, meteor.text[0:i],15)
        pyxel.text(meteor.text_x+i*4, meteor.y-7, meteor.text[i],8)
        pyxel.text(meteor.text_x+(i+1)*4, meteor.y-5, meteor.text[i+1:],15)
        pyxel.blt(meteor.x, meteor.y, 1, 0, 24, 16,16,0)
        
    def draw(self):
        pyxel.cls(0)
        for meteor in self.meteor_list:
            self.draw_meteor(meteor)

        
        

if __name__=="__main__":
    App()
