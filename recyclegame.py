import pgzrun
import random
WIDTH=1210
HEIGHT=908
items = ["bag", "batteryimg", "chipsimg", "bottleimg"]
Level = 1
totallevels=5
actors=[]
animations=[]
def draw():
    global actors
    screen.blit("eco", (0,0))
    for actor in actors:
        actor.draw()
def createactor():
    global items
    global actors
    global actor
    actors.clear()
    paper=Actor("paperimg")
    actors.append(paper)
    for i in range(Level):
        trash=Actor(items[random.randint(0,3)])
        actors.append(trash)
    gaps = Level + 2
    gapsize = WIDTH/gaps
    number = 1
    random.shuffle(actors)
    for actor in actors:
        actor.pos = (number * gapsize, 0)
        number += 1
    #animation
    for actor in actors:
        animation=animate(actor,y = 950, duration = 5, on_finished=gameover)
        animations.append(animation)
def gameover():
    pass
createactor()
def update():
    pass


pgzrun.go()