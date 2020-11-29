import pyxel
from classes.input import *
ON   = 0
DONE = 1

PYXEL = (56, 120, 1, 0 , 80, 48, 16, 0)
GAMEOFF = (120,110,1,0,96,64,32,0)

class Intro:
    def __init__(self):
        self.state = ON
        self.timer = 0
        self.keyboard = Input()
        
    def update(self):
        self.timer +=1
        if self.timer >=200 or self.keyboard.get_input_list():
            self.state = DONE
            
    def draw(self):
        if  self.timer <= 10 or self.timer >182:
            return
        if  10< self.timer <=13:
            for i in range(16):
                pyxel.pal(i,1)

        elif  13< self.timer <=16:
            for i in range(8):
                pyxel.pal(i,5)
            for i in range(8,16):
                pyxel.pal(i,13)
        
            pyxel.pal(11,1)
            pyxel.pal(9,1)

        elif  16< self.timer <=19:
            pyxel.pal(7,12)
            pyxel.pal(11,3)
            pyxel.pal(9,8)
 
        elif  19< self.timer <=22:
            pyxel.pal(7,6)

        elif 22 < self.timer <= 170:
            pass
        elif  170< self.timer <=173:
            pyxel.pal(7,6)
 
        elif  173< self.timer <=176:
            pyxel.pal(7,12)
            pyxel.pal(11,3)
            pyxel.pal(9,8)

        elif  176< self.timer <=179:
            for i in range(8):
                pyxel.pal(i,5)
            for i in range(8,16):
                pyxel.pal(i,13)
        
            pyxel.pal(11,1)
            pyxel.pal(9,1)


        elif  179< self.timer <=182:
            for i in range(16):
                pyxel.pal(i,1)
        pyxel.blt(*PYXEL)
        pyxel.blt(*GAMEOFF)
        pyxel.pal()
