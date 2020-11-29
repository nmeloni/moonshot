import pyxel

class Score:
    def __init__(self):
        self.point = 0
        self.score = 0
        self.combo = 0
        self.index = 0
        self.combo_rule = [0,16,32,64,128,256,512]
        self.combo_point = [1,2,3,4,5,10,20,50] 
        self.multiplier = 0
        
    def update(self):
        pass

    def miss(self):
        self.combo = 0
        
    def hit_char(self):
        self.combo+=1
        i = 0
        while self.combo_rule[i] <= self.combo:
            i +=1
        i -= 1
        self.index = i
        if i<len(self.combo_rule):
            self.point = 100*self.combo_point[i]
        else:
            self.point = 5000
        self.score += self.point
        
    def hit_word(self):
        self.score += 1000

    def hit_sentence(self):
        self.score += 10000
    
    def draw(self):
        pyxel.text(160,2, "score",7)
        pyxel.text(184+40-len(str(self.score)),2,str(self.score),7)
        if self.combo >=16:
            pyxel.text(160,8, "combo x",7)
            if self.index < len(self.combo_point):
                combo = self.combo_point[self.index]
            else:
                combo = 50
            pyxel.text(194,8,str(combo),7)

class Point:
    def __init__(self,x,y,point):
        self.x = x
        self.y = y
        self.point = point
        self.frame = 16

    def update(self):
        self.frame -= 1
        self.y -= 0.5

    def done(self):
        return self.frame <= 0

    def draw(self):
        if self.point < 200:
            color = 15
        elif self.point <500:
            color = 10
        elif self.point <5000:
            color = 8
        elif self.point >=5000:
            color = (pyxel.frame_count % 15) + 1
        pyxel.text(self.x,self.y,str(self.point),color)
