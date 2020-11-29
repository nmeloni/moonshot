import pyxel
from classes.objects import *
from classes.word import *
from classes.input import *

TITLE = 1
PLAY  = 2

class TitleScreen:
    def __init__(self):
        self.stars = stars
        self.keyboard = Input()
        self.start = Word(128,200,"start")
        self.state = TITLE

    def update(self):
        if self.start.is_complete():
            self.state = PLAY
        else:
            self.key_list = self.keyboard.get_input_list()
            if self.start.active_char() in self.key_list:
                self.start.hit()

    def draw(self):
        for star in self.stars:
            if (pyxel.frame_count- star[0]) % 60 == 0: 
                pyxel.line(star[0]-1,star[1],star[0]+1,star[1],7)
                pyxel.line(star[0],star[1]-1,star[0],star[1]+1,7)
            else:
                pyxel.line(star[0],star[1],star[0],star[1],7)
            
        pyxel.blt(0,0,0,0,0,256,256,0)

        pyxel.blt(86,68,1,*T)
        pyxel.blt(98,68,1,*Y)
        pyxel.blt(112,68,1,*P)
        pyxel.blt(124,68,1,*E)
        pyxel.blt(145,68,1,*M)
        pyxel.blt(159,68,1,*E)

        pyxel.blt(118,98,1,*T)
        pyxel.blt(130,98,1,*O)

        pyxel.blt(112,128,1,*T)
        pyxel.blt(124,128,1,*H)
        pyxel.blt(138,128,1,*E)

        pyxel.blt(106,158,1,*M)
        pyxel.blt(120,158,1,*O)
        pyxel.blt(132,158,1,*O)
        pyxel.blt(144,158,1,*N)
        
        
        pyxel.rect(104,194,48,16,0)
        pyxel.text(108,200,"type",15)
        self.start.draw()
