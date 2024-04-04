import turtle
import time
import random

NUM_RINGS = 5
RING_WIDTH_SCALE = 10
RING_HEIGHT = 5
RING_COLORS = []
FILL_COLOR = "red"

window = turtle.Screen()
turtle.colormode(255)

# Example legal tower: [5,4,3,2,1]
class Tower:
    def __init__(self, startingRings, ringCapacity, towerNum):
        self.rings = startingRings
        self.maxRings = ringCapacity
        self.num = towerNum

        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.t.penup()
        self.t.backward(RING_WIDTH_SCALE * (self.maxRings+1))
        self.t.forward(RING_WIDTH_SCALE * (self.maxRings+1) * self.num)
    def addRing(self, num):
        if len(self.rings) + 1 > self.maxRings:
            print("Tried to put too many rings on a tower!")
        elif len(self.rings) > 0 and self.rings[-1] < num:
            print("Tried to put a bigger ring on top of a smaller ring!")
        else:
            self.rings.append(num)
    def removeRing(self):
        return self.rings.pop(-1)
    def moveRing(self, other):
        other.addRing(self.removeRing())
    def drawTower(self):
        self.t.clear()
        window.tracer(0)
        self.t.penup()
        for ring in self.rings:
            self.t.fillcolor(RING_COLORS[ring-1])
            self.t.backward(RING_WIDTH_SCALE * ring / 2.0)
            self.t.pendown()
            self.t.begin_fill()
            self.t.forward(RING_WIDTH_SCALE * ring)
            self.t.left(90)
            self.t.forward(RING_HEIGHT)
            self.t.left(90)
            self.t.forward(RING_WIDTH_SCALE * ring)
            self.t.left(90)
            self.t.forward(RING_HEIGHT)
            self.t.end_fill()
            self.t.penup()
            self.t.left(180)
            self.t.forward(RING_HEIGHT)
            self.t.right(90)
            self.t.forward(RING_WIDTH_SCALE * ring / 2.0)
        self.t.right(90)
        self.t.forward(RING_HEIGHT * len(self.rings))
        self.t.left(90)
        window.update()

def drawTowers(towers):
    towers[0].drawTower()
    towers[1].drawTower()
    towers[2].drawTower()
    time.sleep(0.5)
    

def moveStack(towers, num_rings, from_tower, to_tower, other_tower):
    ft = towers[from_tower]
    tt = towers[to_tower]
    ot = towers[other_tower]
    
    if num_rings == 1: # Base case:
        ft.moveRing(tt)
        drawTowers(towers)
    else: # Recursive case
        # Move top over to other tower
        moveStack(towers, num_rings-1, from_tower, other_tower, to_tower)
        # Move bottom ring to to tower
        ft.moveRing(tt)
        drawTowers(towers)
        # Move top to to tower
        moveStack(towers, num_rings-1, other_tower, to_tower, from_tower)

    
    

if __name__ == '__main__':
    rings_list = []
    for i in range(NUM_RINGS):
        RING_COLORS.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    for i in range(NUM_RINGS,0,-1):
        rings_list.append(i)
    t0 = Tower(rings_list,NUM_RINGS,0)
    t1 = Tower([],NUM_RINGS,1)
    t2 = Tower([],NUM_RINGS,2)
    drawTowers([t0,t1,t2])
    moveStack([t0,t1,t2],NUM_RINGS,0,2,1)
    window.mainloop()
