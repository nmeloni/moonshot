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

MT_BULLET_SPEED = 5

POEME = ["la","nuit","je","mens","je","prends","des","trains","a","travers","la","pleine"]

class Meteor():
    def __init__(self, x,y, text):
        self.x = x
        self.y = y
        self.dy = (1,2)
        self.is_active = False
        self.is_complete = False
        self.text = text
        self.text_x = x+8 - len(text)*2
        self.text_y = y-8
        self.active_letter = 0
        self.hit_frame = 0
        self.hit_point = len(text)

    def update(self):
        if pyxel.frame_count % self.dy[1] == 0:
            self.y+=self.dy[0] 
        self.hit_frame = max(0,self.hit_frame-1)
        
    def hit(self):
        self.active_letter += 1
        if self.active_letter == len(self.text):
            self.is_complete = True


class Bullet():
    def __init__(self,x,y,dx,dy,meteor):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.meteor = meteor

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def hit(self):
        if abs(self.meteor.x+4-self.x) <= 8 and \
           abs(self.meteor.y+4-self.y) <= 8 :
            self.meteor.hit_point -= 1
            self.meteor.hit_frame = 4
            return True
        else:
            return False

    def destroy(self):
        return self.meteor.hit_point == 0

class Explosion():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame = 5
        
    def update(self):
        self.frame -= 1
    
class App():
    def __init__(self):
        pyxel.init(MT_SCREEN_X,MT_SCREEN_Y, caption="--- MOONTYPE --- ")
        pyxel.load("moontype.pyxres")


        self.poem = POEME[::-1]
        self.meteor_list = [Meteor(randrange(16,240),0,self.poem.pop())]
        self.meteor_list[0].active = True

        self.bullet_list = []
        self.explosion_list = []
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if (pyxel.frame_count % 60 == 0) and (len(self.poem)!=0):
            self.meteor_list.insert(0,Meteor(randrange(16,240),0,self.poem.pop()))
            
        for meteor in self.meteor_list:
            meteor.update()

        for explosion in self.explosion_list:
            explosion.update()

        while len(self.explosion_list) != 0 and self.explosion_list[-1].frame == 0:    
            self.explosion_list.pop()

        for bullet in self.bullet_list:
            bullet.update()
            if bullet.hit():
                print("hit")
                if bullet.destroy():
                    print("destroy")
                    self.explosion_list.insert(0,Explosion(bullet.meteor.x,bullet.meteor.y))
                    self.meteor_list.remove(bullet.meteor)
                self.bullet_list.remove(bullet)

        if len(self.meteor_list) != 0:
            for meteor in self.meteor_list[::-1]:
                if meteor.is_complete:
                    continue
                meteor.is_active = True
                letter = meteor.text[meteor.active_letter]
                # if the button corresponds to the active letter
                if pyxel.btn( ord(letter)-MT_ASCII_KEY_OFFSET+MT_PYXEL_KEY_OFFSET ):
                    # modify active letter
                    meteor.hit()
                    #compute direction and emit a bullet
                    x_B,y_B = MT_SCREEN_X//2,MT_SCREEN_Y
                    x_M,y_M = meteor.x+8, meteor.y+8
                    if x_M == x_B:
                        dx,dy = 0,4
                    else:
                        r = (y_M-y_B)/(x_M-x_B)
                        V_M = meteor.dy[0]/meteor.dy[1]
                        A,B,C = 1 + r*r, 2*r*V_M, V_M*V_M - MT_BULLET_SPEED*MT_BULLET_SPEED
                        beta = (B**2-4*A*C)**0.5
                        if (x_B-x_M) > 0:
                            dx = (-B - beta)/(2*A)
                        else:
                            dx = (-B + beta)/(2*A)
                        dy = (MT_BULLET_SPEED*MT_BULLET_SPEED - dx*dx)**0.5
                    bullet = Bullet(x_B,y_B,dx,-dy,meteor)
                    self.bullet_list.append(bullet)
                break
                

        
    def draw_meteor(self, meteor):
        
        if meteor.is_active:
            if meteor.is_complete:
                 pyxel.text(meteor.text_x, meteor.y-7, meteor.text,pyxel.frame_count % 15 + 1)
            else:
                i = meteor.active_letter
                pyxel.text(meteor.text_x, meteor.y-5, meteor.text[0:i],15)
                pyxel.text(meteor.text_x+i*4, meteor.y-7, meteor.text[i],8)
                pyxel.text(meteor.text_x+(i+1)*4, meteor.y-5, meteor.text[i+1:],15)
        else:
            pyxel.text(meteor.text_x, meteor.y-7, meteor.text,15)
                    
        if meteor.hit_frame ==0:
            pyxel.blt(meteor.x, meteor.y, 1, 0, 24, 16,16,0)
        elif meteor.hit_frame  == 1 or meteor.hit   == 3:
            pyxel.blt(meteor.x, meteor.y, 1, 16, 24, 16,16,0)
        else:
            pyxel.blt(meteor.x, meteor.y, 1, 32, 24, 16,16,0)

    def draw_bullet(self, bullet):
        pyxel.circ(bullet.x,bullet.y,2, (pyxel.frame_count % 15)+1)

    def draw_explosion(self, explosion):
        pyxel.blt(explosion.x, explosion.y, 1, 48+16*(5-explosion.frame), 24, 16,16,0)
        
    def draw(self):
        pyxel.cls(0)
        for meteor in self.meteor_list:
            self.draw_meteor(meteor)
        for bullet in self.bullet_list:
            self.draw_bullet(bullet)
        for explosion in self.explosion_list:
            self.draw_explosion(explosion)

if __name__=="__main__":
    App()
