import pyxel

class Sprite:
    def __init__(self,img,u,v,w,h,key,colors=None):
        self.img  = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.key = key
        self.colors = colors

    def draw(self,x,y):
        if self.colors:
            for c1,c2 in self.colors:
                pyxel.pal(c1,c2)
        pyxel.blt(x,y,self.img,self.u,self.v,self.w,self.h,self.key)
        pyxel.pal()



    
