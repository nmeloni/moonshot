import pyxel
from classes.word import *
from classes.destruction import *
from classes.explosion import *
from classes.animation import *
from classes.sprite import *
from classes.rock import *
from classes.objects import *
from random import randrange

from copy import deepcopy

FO_FALLING   =  0
FO_DESTROYED =  1
FO_FAIL = 2

class FallingObject:
    def __init__(self,x,y,dx=0,dy=0,ddx=0,ddy=0,maxspeed=1):
        self.x = x
        self.y = y
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = ddx
        self.ddy = ddy
        self.maxspeed = maxspeed
        self.state = FO_FALLING
        self.nb_miss = 0

    def set_xy(self,x,y):
        self.x = x
        self.y = y

    def set_dxdy(self,dx,dy):
        self.dx = dx
        self.dy = dy

    def set_ddxddy(self,ddx,ddy):
        self.ddx = ddx
        self.ddy = ddy

    def hit(self):
        pass

    def physics(self):
        if self.dx < 0:
            self.dx = min(0, self.dx - self.ddx)
        else:
            self.dx = max(0, self.dx + self.ddx)
        self.dy = min(self.maxspeed, self.dy + self.ddy)
        
            
        
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def miss(self):
        self.nb_miss += 1

    def get_state(self):
        return self.state
    
    def set_state(self,state):
        self.state = state
        
class SimpleFO(FallingObject):
    def __init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion=None):
        FallingObject.__init__(self,x,y,dx,dy,ddx,ddy,maxspeed)
        self.word = word
        
        self.rock = rock
        self.explosion = explosion

    def hit(self):
        self.word.hit()
        self.rock.hit()
        
    def active_char(self):
        return self.word.active_char()
    
    def get_target(self):
        x = self.rock.x+self.rock.sprite.w//2
        y = self.rock.y+self.rock.sprite.h//2
        return x,y
        
    def update(self):
        self.physics()
        self.move()
        self.word.active_char()
        if self.word.is_complete():
            self.state = FO_DESTROYED
            return
        self.rock.update()
        self.word.set_xy(self.x,self.y)
        self.rock.set_xy(self.x+len(self.word.text)*2 - self.rock.sprite.w//2, self.y +8)

    def draw(self):
        self.word.draw()
        self.rock.draw()

    def destroy(self):
        if self.explosion:
            self.explosion.set_xy(self.x+len(self.word.text)*2 - self.rock.sprite.w//2, self.y +8)
        explosions = [self.explosion]
        if self.state == FO_DESTROYED:
            if self.nb_miss == 0:
                color = CLR_TWINK
            else:
                color = CLR_MISS
        else:
            color = CLR_FAIL
        self.word.set_state(W_DONE)
        self.word.set_color(color)
        return Desctruction(explosions, [])

class MirrorFO(SimpleFO):
    def __init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion=None):
        SimpleFO.__init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion)
        self.word.set_order([i for i in range(len(self.word.text)-1,-1,-1)])

class RandomFO(SimpleFO):
    def __init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion=None):
        SimpleFO.__init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion)
        l = [i for i in range(len(self.word.text))]
        order = [l.pop(randrange(len(l))) for i in range(len(self.word.text))]
        self.word.set_order(order)
    
class SplitFOsmall(SimpleFO):
    def __init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion=None):
        SimpleFO.__init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion)
        
    def destroy(self):
        if self.explosion:
            self.explosion.set_xy(self.x+len(self.word.text)*2 - self.rock.sprite.w//2, self.y +8)
        explosions = [self.explosion]
        if self.state == FO_DESTROYED:
            if self.nb_miss == 0:
                color = CLR_TWINK
            else:
                color = CLR_MISS
        else:
            color = CLR_FAIL
        self.word.set_state(W_DONE)
        self.word.set_color(color)
        if self.state == FO_FAIL:
            return Desctruction(explosions,[])
        letters = list(self.word.text)
        n = len(letters)
        v = splits_vxy[:]
        v_xy = [ v.pop(randrange(len(v))) for i in range(n)]
        fos = []
        for i in range(len(letters)):
            c = letters[i]
            w=Word(0,0,c)
            speed = (*v_xy[i],-0.08, 0.11, 0.4+randrange(10)/10)
            obj = (0, SIMPLE, 0,speed,stone_list,hit_anim,stone_expl_anim)
            obj = make_SimpleFO(obj,w)
            obj.set_xy(self.x,self.y)
            fos.append(obj)
        return Desctruction(explosions,fos)

    def draw(self):
        self.word.draw()
        pyxel.pal(5,3)
        pyxel.pal(12,11)
        self.rock.draw()
        pyxel.pal()



class MeteorFO(FallingObject):
    def __init__(self,x,y,dx,dy,ddx,ddy,maxspeed,words,rock,expl):
        FallingObject.__init__(self,x,y,dx,dy,ddx,ddy,maxspeed)
        self.word_list = words
        self.words_state = W_BASE
        self.active_word_i = 0
        self.active_word = self.word_list[0]
        
        self.rock = rock
        self.explosion = expl

    def hit(self):
        self.active_word.hit()
        self.rock.hit()

    def active_char(self):
        return self.active_word.active_char()
    
    def get_target(self):
        x = self.rock.x+self.rock.sprite.w//2+(randrange(2)-1)*self.rock.sprite.w//4
        y = self.rock.y+self.rock.sprite.h//2+(randrange(2)-1)*self.rock.sprite.h//4
        return x,y

    def update(self):
        self.physics()
        self.move()
        if self.active_word.is_complete():
            self.active_word_i += 1
        if self.active_word_i == len(self.word_list):
            self.state = FO_DESTROYED
            return
        self.active_word = self.word_list[self.active_word_i]
        self.rock.update()
        acc = 0
        for w in self.word_list:
            w.set_xy(self.x+acc,self.y)
            acc += (len(w.text)+1)*4
        acc -=4
        self.rock.set_xy(self.x+acc//2 - self.rock.sprite.w//2, self.y +8)

    def draw(self):
        for word in self.word_list:
            word.draw()
        self.rock.draw()

    def destroy(self):
        rock_anim = Animation([self.rock.sprite],[0,0,0,0])
        rock_expl = Explosion(self.rock.x,self.rock.y,rock_anim)
        explosions = [deepcopy(self.explosion) for i in range(5)]
        for i in range(5):
            explosions[i].set_xy(self.rock.x +i*self.rock.sprite.w//5, self.y + 8+randrange(3)*self.rock.sprite.h//6)
            explosions[i].delay = randrange(10)*2

        explosions = [rock_expl]+explosions 
        if self.state == FO_DESTROYED:
            if self.nb_miss == 0:
                color = CLR_TWINK
            else:
                color = CLR_MISS
        else:
            color = CLR_FAIL
        for word in self.word_list:
            word.set_state(W_DONE)
            word.set_color(color)
        return Desctruction(explosions, [])


    
class SplitFObonus(SimpleFO):
    def __init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion=None):
        SimpleFO.__init__(self,x,y,dx,dy,ddx,ddy,maxspeed,word,rock,explosion)
        print("init")
        
    def destroy(self):
        if self.explosion:
            self.explosion.set_xy(self.x+len(self.word.text)*2 - self.rock.sprite.w//2, self.y +8)
        explosions = [self.explosion]
        if self.state == FO_DESTROYED:
            if self.nb_miss == 0:
                color = CLR_TWINK
            else:
                color = CLR_MISS
        else:
            color = CLR_FAIL
        self.word.set_state(W_DONE)
        self.word.set_color(color)

        code = [pyxel.KEY_UP,pyxel.KEY_UP,pyxel.KEY_DOWN,pyxel.KEY_DOWN,pyxel.KEY_LEFT,pyxel.KEY_RIGHT,pyxel.KEY_LEFT,pyxel.KEY_RIGHT,pyxel.KEY_B,pyxel.KEY_A]
        w=Code(0,0,code)
        speed = (0,-1.4,0, 0.08, 0.5)
        obj = (0,SIMPLE, 0,speed, [LIFE], hit_anim, tiny_expl_anim)
        obj = make_SimpleFO(obj,w)
        obj.set_xy(self.x, self.y)
        return Desctruction(explosions, [obj])

def make_SimpleFO(obj,w):
    if len(w.text)<2:
        rl = stone_list
        el = stone_expl_anim
    elif len(w.text)<5:
        rl = rock_list
        el = tiny_expl_anim
    elif len(w.text)<8:
        rl = big_rock_list
        el = expl_anim
    else:
        rl = huge_rock_list
        el = expl_anim
        
    rock = rl[randrange(len(rl))]
    s1 = Sprite(*rock)
    s2 = Sprite(*rock,hit_anim[0][0])
    s3 = Sprite(*rock,hit_anim[0][1])
    idle = Animation([s1],[0])
    hit = Animation([s1,s2,s3],hit_anim[1])
    expl = Animation([Sprite(*el[0][i]) for i in range(len(el[0]))],el[1])
    e = Explosion(0,0,expl)
    r = Rock(0,0,idle,hit)
    x,y = min(256-len(w.text)*4,max(0,obj[2]+25+s1.w//2-len(w.text)*2)), -s1.h
    if obj[1] == SIMPLE:
        fo = SimpleFO(x,y,*obj[3],w,r,e)
    elif obj[1] == MIRROR:
        fo = MirrorFO(x,y,*obj[3],w,r,e)
    elif obj[1] == RANDOM:
        fo = RandomFO(x,y,*obj[3],w,r,e)
    elif obj[1] == SPLITS:
        fo = SplitFOsmall(x,y,*obj[3],w,r,e)
    elif obj[1]== BONUS:
        fo = SplitFObonus(x,y,*obj[3],w,r,e)
    return fo

def make_MeteorFO(obj,w):
    rl = meteor_list
    el = expl_anim
    rock = rl[randrange(len(rl))]
    s1 = Sprite(*rock)
    s2 = Sprite(*rock,hit_anim[0][0])
    s3 = Sprite(*rock,hit_anim[0][1])
    idle = Animation([s1],[0])
    hit = Animation([s1,s2,s3],hit_anim[1])
    expl = Animation([Sprite(*el[0][i]) for i in range(len(el[0]))],el[1])
    e = Explosion(0,0,expl)
    r = Rock(0,0,idle,hit)
    lgth = sum(len(word.text) for word in w)
    x,y = max(0,obj[2]+s1.w//2-lgth*2), -s1.h
    fo = MeteorFO(x,y,*obj[3],w,r,e)
    return fo


