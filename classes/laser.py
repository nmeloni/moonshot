import pyxel

class Laser():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame = 6
        
    def update(self):
        self.frame -=1

    def done(self):
        return self.frame <= 0
        
class LaserHit(Laser):
    def __init__(self,x,y):
       Laser.__init__(self,x,y)

    def draw(self):
        if self.frame == 5:
            pyxel.circ(128,256,4,7)
        if self.frame == 4:
            pyxel.circ(128,256,5,11)
            pyxel.circ(128,256,4,7)
        if self.frame == 3:
            pyxel.circ(128,256,6,6)
            pyxel.circ(128,256,5,11)
            pyxel.circ(128,256,4,7)
            pyxel.line(128,255,self.x,self.y,7)
            pyxel.circb(self.x,self.y,1,7)
            
        if self.frame == 2:
            pyxel.circb(128,256,6,6)
            pyxel.circb(128,256,5,11)
            pyxel.line(128,255,self.x,self.y,7)
            pyxel.line(127,255,self.x-1,self.y,11)
            pyxel.line(129,255,self.x+1,self.y,11)
            pyxel.circb(self.x,self.y,2,7)

        if self.frame == 1:
            pyxel.circb(128,256,6,6)
            pyxel.line(128,255,self.x,self.y,7)
            pyxel.circb(self.x,self.y,3,7)

class LaserMiss(Laser):
    def __init__(self,x,y):
        Laser.__init__(self,x,y)
        
    def draw(self):
        if self.frame == 5:
            pyxel.circ(128,256,4,7)
        if self.frame == 4:
            pyxel.circ(128,256,5,8)
            pyxel.circ(128,256,4,7)
            
        if self.frame == 3:
            pyxel.circ(128,256,6,2)
            pyxel.circ(128,256,5,8)
            pyxel.circ(128,256,4,7)
          
        if self.frame == 2:
            pyxel.circb(128,256,6,2)
            pyxel.circb(128,256,5,8)
          
        if self.frame == 1:
            pyxel.circb(128,256,6,2)
