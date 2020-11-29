class Explosion:
    def __init__(self,x,y,explosion,rock=None,delay=0):
        self.x = x
        self.y = y
        self.delay = delay
        self.anim = explosion
        self.sprite = explosion.get_sprite()
        self.rock = rock
        self.timer = 0
        
    def update(self):
        self.timer +=1
        if self.timer >= self.delay:
            self.anim.update()
            self.sprite = self.anim.get_sprite()
        
    def draw(self):
        if not self.anim.done():
            self.sprite.draw(self.x,self.y)

    def done(self):
        return self.anim.done()

    def set_xy(self,x,y):
        self.x = x
        self.y = y
