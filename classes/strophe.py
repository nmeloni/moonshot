from classes.word import *

STR_DURATION = 240

STR_BASE = 0
STR_COMPLETED = 1


class Strophe():
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.words = []
        self.coord = []
        self.state = STR_BASE
        self.vanish = False
        self.timer = 0
        lines = s.splitlines()
        for i in range(len(lines)):
            l = lines[i].split()
            for j in range(len(l)):
                l[j]= Word(0,0,l[j])
                self.coord.append((i,j))
            self.words.append(l)

    def set_xy(self,x,y):
        self.x = x
        self.y = y

    def pop_word(self):
        i,j = self.coord.pop(0)
        return self.words[i][j]

    def get_word(self,i,j):
        return self.words[i][j]

    def get_state(self):
        return self.state
    
    def done(self):
        return self.vanish

    def is_empty(self):
        return self.coord == []
    
    def update(self):
        if self.state == STR_COMPLETED:
            self.timer += 1
            if self.timer > STR_DURATION:
                self.vanish = True
            return
        complete = True
        moving = False
        for i in range(len(self.words)):
            acc = self.x
            for j in range(len(self.words[i])):
                w = self.words[i][j]
                x,y = acc ,self.y+i*12
                acc = x+ (len(w.text)+1)*4
                if w.get_state() == W_DONE:
                    if abs(w.x-x)>=0.5 or abs(w.y-y)>=0.5:
                        moving = True
                        if abs(w.x-x)<0.5:
                            dx = 0
                            if y > w.y:
                                dy = 1.5
                            else:
                                dy = -1.5
                        else:
                            if x > w.x:
                                dx = 1.5
                            else:
                                dx = -1.5
                            dy = (y-w.y)/abs(x-w.x)
                            if dy > 2:
                                dy = 2
                            if dy < -2:
                                dy = -2
                        w.move(dx,dy)
                    if abs(w.x-x)<1:
                        w.x = x
                    if abs(w.y-y)<1:
                        w.y = y
                else:
                    complete = False    
        if complete and not moving:
            self.state = STR_COMPLETED
            self.timer = 0

    def draw(self):
        first = int ((self.timer/STR_DURATION)*len(self.words))
        for i in range(first, len(self.words)):
            acc = self.x
            for j in range(len(self.words[i])):
                w = self.words[i][j]
                if w.get_state() == W_DONE:
                    w.draw()
    
    
