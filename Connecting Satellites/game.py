import pgzrun
import random
import time

WIDTH, HEIGHT, TITLE= 1500,1000,'Connecting Satellites'

satellites=[]
numsatellite = 3
lines=[]
next= 0
starttime=0
totaltime=0


def createsatellites():
    global starttime
    for x in range(0,numsatellite):
        satellite = Actor('satellite')
        satellite.pos = (random.randint(50,WIDTH-50), random.randint(50,HEIGHT-50))
        satellites.append(satellite)
    starttime = time.time()


def on_mouse_down(pos):
    global lines, next
    if next<numsatellite:
        if satellites[next].collidepoint(pos):
            if next:
                lines.append((satellites[next-1].pos, satellites[next].pos))
            next+=1
        else:
            next = 0
            lines= []


createsatellites()

def update():
   pass

def draw():
    global next,totaltime, starttime
    screen.clear()
    screen.blit("sky", (0,0))
    number = 1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20),)
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],color = (255,255,255))
    if next==numsatellite:
        gameOver()
    else:
        screen.draw.text('Time: '+ str(int(time.time()-starttime)), (50,50),color= (100,100,200), fontsize=30)
        totaltime=int(time.time()-starttime)

def gameOver():
    global totaltime
    screen.fill(color=(150,100,100))
    screen.draw.text('Nice Work!\nYou took '+ str(totaltime)+ ' seconds', (WIDTH/2, HEIGHT/2), color= (255,255,255),fontsize=70)


pgzrun.go()

