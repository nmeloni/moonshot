import pyxel
from classes.objects import *

W_BASE = 0
W_ACTIVE = 1
W_DONE = 2

CLR_BASE = 15
CLR_HIT  = 8
CLR_TWINK = 16
CLR_MISS = 6
CLR_FAIL = 13

class Word:
    def __init__(self,x,y,text,color=CLR_BASE,order=None):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.active_index = 0
        self.state = W_BASE
        if order:
            self.order = order
        else:
            self.order = [i for i in range(len(text))]

    def set_xy(self,x,y):
        self.x = x
        self.y = y
        
    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def set_order(self, order):
        self.order = order
        
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def set_color(self,color):
        self.color = color
        
    def get_index(self):
        return self.active_index

    def hit(self):
        self.set_state(W_ACTIVE)
        self.inc_index()

    def inc_index(self):
        self.active_index += 1

    def active_char(self):
        if self.active_index < len(self.text):
            return ord(self.text[self.active_index])-ord('a')+pyxel.KEY_A
        return None
    
    def is_complete(self):
        return self.active_index == len(self.text)
    
    def draw(self):
        if self.state == W_ACTIVE:
            for i in range(len(self.text)):
                if self.order[i]<self.active_index:
                    color = CLR_HIT
                else:
                    color = CLR_BASE
                pyxel.text(self.x+i*4, self.y, self.text[self.order[i]],color)
        else:
            if self.color == CLR_TWINK:
                color = pyxel.frame_count %15 + 1
            else:
                color = self.color
            if self.state == W_BASE:
                for i in range(len(self.text)):
                    pyxel.text(self.x+i*4, self.y, self.text[self.order[i]],color)
            else:
                pyxel.text(self.x,self.y,self.text,color)

class Code(Word):
    def __init__(self,x,y,code,color=CLR_BASE):
        self.x = x
        self.y = y
        self.text = code
        self.color = color
        self.active_index = 0
        self.state = W_BASE
        
    def active_char(self):
        if self.active_index < len(self.text):
            return self.text[self.active_index]
        return None

    def draw(self):
        if self.state == W_ACTIVE:
            for i in range(len(self.text)):
                if i < self.active_index:
                    color = CLR_HIT
                else:
                    color = CLR_BASE
                key = self.text[i]
                pyxel.pal(7,color)
                pyxel.blt(self.x+i*6, self.y, *CODE[key])
                pyxel.pal()
        else:
            if self.color == CLR_TWINK:
                color = pyxel.frame_count %15 + 1
            else:
                color = self.color
            for i in range(len(self.text)):
                key = self.text[i]
                pyxel.pal(7,color)
                pyxel.blt(self.x+i*6, self.y, *CODE[key])
                pyxel.pal()

            
