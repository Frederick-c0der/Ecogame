import pgzrun
import random
WIDTH=1210
HEIGHT=908
items = ["bag", "batteryimg", "chipsimg", "bottleimg"]
Level = 1
totallevels=5
gameover = False
finished=False
actors=[]
animations=[]
def draw():
    global actors
    screen.blit("eco", (0,0))
    for actor in actors:
        actor.draw()
    if gameover==True:
        screen.draw.text("GAME OVER", (605,454), color="white")
    if finished == True:
        screen.draw.text("YOU WON!", (605,454), color="white")
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
def nextlevel():
    global finished
    global Level
    stopfunction()
    if Level==totallevels:
        finished=True
    else: 
        Level += 1
        createactor()
def game_over():
    global gameover
    gameover = True
createactor()
def stopfunction():
    global animations
    for animation in animations:
        if animation.running:
            animation.stop()
def update():
    if gameover==True:
        stopfunction()
def on_mouse_down(pos):
    global items 
    for actor in actors:
        if actor.collidepoint(pos):
            if "paperimg" in actor.image:
                nextlevel()
            else:
                game_over()


pgzrun.go()