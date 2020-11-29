import pyxel
from classes.sprite import *
from random import randrange

class Background:
    def __init__(self):
        self.hit_frame = 0
        self.hp = 10
        self.hit_anim = [(1,5,12,12,12),(8,1,5,5,5),(10,8,1,1,1),(9,10,8,8,8),(8,9,10,10,10),(12,8,9,9,9),(5,12,8,8,8)]
        self.hp_color = [(2,8,9,14,15),
                         (1,8,9,14,15),(1,8,9,14,15),
                         (1,5,9,14,15),(1,5,9,14,15),
                         (1,5,12,14,15),(1,5,9,14,15),
                         (1,5,12,6,15),(1,5,12,6,15),
                         (1,5,12,6,7), (1,5,12,6,7)]
        
        self.stars1 = [[x*16+randrange(8), randrange(256)] for x in range(16)]
        self.stars2 = [[x*16+randrange(8), randrange(256)] for x in range(16) ]
        self.stars3 = [[x*16+randrange(8), randrange(256)] for x in range(16) ]

        self.earth = Sprite(2,11,0,244,48,0)

    def hit(self):
        self.hit_frame = 6

    def set_hp(self,hp):
        self.hp = hp
        
    def update(self):
        self.hit_frame = max(0,self.hit_frame-1)
        for star in self.stars1:
            star[1] = (star[1]+0.25)%256
        for star in self.stars2:
            star[1] = (star[1]+0.5)%256
        for star in self.stars3:
            star[1] = (star[1]+1)%256

    def draw(self):
        if self.hit_frame:
            col = self.hit_anim[self.hit_frame]
        else:
            col = self.hp_color[self.hp]
        pyxel.circ(128,452,256,col[0])
        pyxel.circ(128,464,256,col[1])
        pyxel.circ(128,472,256,col[2])
        pyxel.circ(128,475,256,col[3])
        pyxel.circ(128,478,256,col[4])
        for star in self.stars1:
            pyxel.line(star[0],star[1],star[0],star[1],5)
        for star in self.stars2:
            pyxel.line(star[0],star[1],star[0],star[1]+1,12) 
        for star in self.stars3:
            pyxel.line(star[0],star[1],star[0],star[1]+1,7)
        
        self.earth.draw(11,220)
