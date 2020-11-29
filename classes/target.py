import pyxel
from classes.sprite import *

class Target:
    def __init__(self,x,y,img,u,v,w,h,key):
        Sprite.__init__(self,img,u,v,w,h,key)
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x,self.y,self.img,self.u,self.v,self.w,self.h,self.key)
