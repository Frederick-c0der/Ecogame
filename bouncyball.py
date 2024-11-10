import pgzrun 
WIDTH=600
HEIGHT=600
class Sphere():
    def __init__(self,r,c,x,y):
        self.radius=r
        self.color=c
        self.x=x
        self.y=y
        self.vx=2
        self.vy=0
        self.gravity=200
    def circledraw(self):
        screen.draw.filled_circle((self.x,self.y), self.radius, self.color) 
ball1=Sphere(50,"blue",100,100)
def draw():
    screen.fill("black")
    ball1.circledraw()
def update(dt):
    uy=ball1.vy
    ball1.vy=ball1.vy+ball1.gravity*dt
    ball1.y=ball1.y+(uy+ball1.vy)*0.5*dt
    
pgzrun.go()