from tkinter import *
from tkinter import messagebox
from random import *
import math

def key(event):
    tmp = int(str(repr(event.char))[len(str(repr(event.char)))-2])
    slide(DIRECTIONS[tmp])

def restart():
    global firstTwo
    global grid
    global score
    
    firstTwo = [math.floor(random()*16) for i in range(2)]
    while (firstTwo[0] == firstTwo[1]):
        firstTwo[1] = math.floor(random()*16)

    grid = [[GridObject(i,j,0) for i in range(4)] for j in range(4)]

    score = 0

    canvas.delete(ALL)

    newGame = Button(root, text ="New Game", command=restart, font=("Arial",20), width = int((size-2*(size-border*1.25)/4)/10+5))
    newGameWindow = canvas.create_window((size-border*1.25)/8, (size-border*1.25)/64, anchor=NW, window=newGame)

    scoreBg = canvas.create_rectangle((size-border*1.25)/8, (size-border*1.25)/16+5, 5+2*border+(math.floor((size-border*1.25)/16)*len("Score: " + str(score)))/2, (size-border*1.25)/16+2*math.floor((size-border*1.25)/16), fill = '#ecf0f1')
    scoreObj = canvas.create_text((size-border*1.25)/8+5+border/2, (size-border*1.25)/16+math.floor((size-border*1.25)/16), text = "Score: " + str(score), font = ("Arial", math.floor((size-border*1.25)/16)), anchor=W)

    for i in range(4):
        for j in range(4):

            textSize = (size-border*1.25)/8
            num = len(str(grid[i][j].value))
            textSize = textSize/num

            grid[i][j].draw()
    
def slide(direction):

    global hasContinued
    global grid
    global textSize
    global score
    
    prevGrid = grid
    newGrid = [[],[],[],[]]

    for i in range(4):
        for j in range(4):
            if (grid[i][j].value != 0):
                newGrid[i if (direction == "left" or direction == "right") else j].append(GridObject(j, i, grid[i][j].value))

        
    for i in range(4):
        counter= 3 if direction=="right" or direction=="down" else 0
        prevJ=None
        prevI=None
        prevValue=None
        if (direction == "right" or direction == "down"):
            for j in range(len(newGrid[i])-1, -1, -1):
                if (j < 0):
                    break
                
                if (prevJ != None and newGrid[i][j].value == prevValue):
                    newGrid[prevI][prevJ].value += newGrid[i][j].value
                    score += newGrid[i][j].value
                    newGrid[i].pop(j)
                    prevValue = None
                    prevI = None
                    prevJ = None
                else:
                    if (direction == "down"):
                        newGrid[i][j].y=counter
                    else:
                        newGrid[i][j].x=counter
                    counter-=1
                    prevValue = newGrid[i][j].value
                    prevI = i
                    prevJ = j
        else:
            j=0
            while(j < len(newGrid[i])):
                if (j >= len(newGrid[i])):
                    break
                
                if (prevJ != None and newGrid[i][j].value == prevValue):
                    newGrid[prevI][prevJ].value += newGrid[i][j].value
                    score += newGrid[i][j].value
                    newGrid[i].pop(j)
                    j-=1
                    prevValue = None
                    prevI = None
                    prevJ = None
                else:
                    if (direction == "up"):
                        newGrid[i][j].y=counter
                    else:
                        newGrid[i][j].x=counter
                    counter+=1
                    prevValue = newGrid[i][j].value
                    prevI = i
                    prevJ = j
                j+=1


    grid = [[GridObject(i,j,1) for i in range(4)] for j in range(4)] 

    for i in range(4):
        for j in range(len(newGrid[i])):
            grid[newGrid[i][j].y][newGrid[i][j].x] = newGrid[i][j]

    for i in grid:
        for j in i:
            if (j.value == 2048 and not hasContinued):
                result = messagebox.askyesno("You win!","Would you like to continue?")
                if (result):
                   hasContinued = True
                   break
                else:
                    result = messagebox.askyesno("Restart","Would you like to restart?")
                    if (result):
                        restart()
                    else:
                        root.destroy()
    zero = False
    for i in range(4):
        for j in range(4):
            if(grid[i][j].value == 0):
                zero = True
                break

    if(zero and not [[x.value for x in y] for y in grid] == [[x.value for x in y] for y in prevGrid]):
        randomXtra = math.floor(random()*16)
        while (grid[math.floor(randomXtra/4)][randomXtra%4].value != 0):
            randomXtra = math.floor(random()*16)
            
        grid[math.floor(randomXtra/4)][randomXtra%4] = GridObject(randomXtra%4, math.floor(randomXtra/4), [2,4][math.floor(random()*2)])

    newGrid = []

    lost = True
    for i in range(4):
        for j in range(4):
            if((i+1 < 4 and grid[i][j].value == grid[i+1][j].value) or (j+1 < 4 and grid[i][j].value == grid[i][j+1].value) or zero):
                lost = False
                break
                        
    if(lost):
        result = messagebox.askyesno("You lose!","Would you like to retry?")
        if (result):
            restart()
        else:
            root.destroy()
            

    canvas.delete(ALL)

    newGame = Button(root, text ="New Game", command=restart, font=("Arial",20), width = int((size-2*(size-border*1.25)/4)/10+5))
    newGameWindow = canvas.create_window((size-border*1.25)/8, (size-border*1.25)/64, anchor=NW, window=newGame)

    scoreBg = canvas.create_rectangle((size-border*1.25)/8, (size-border*1.25)/16+5, 5+2*border+(math.floor((size-border*1.25)/16)*len("Score: " + str(score)))/2, (size-border*1.25)/16+2*math.floor((size-border*1.25)/16), fill = '#ecf0f1')
    scoreObj = canvas.create_text((size-border*1.25)/8+5+border/2, (size-border*1.25)/16+math.floor((size-border*1.25)/16), text = "Score: " + str(score), font = ("Arial", math.floor((size-border*1.25)/16)), anchor=W)

    for i in range(4):
        for j in range(4):
        
            textSize = (size-border*1.25)/8
            num = len(str(grid[i][j].value))
            textSize = textSize/num

            grid[i][j].draw()
    
class GridObject:
    
    def __init__ (self,  gridx, gridy, value):

        if (gridy*4+gridx in firstTwo):
            self.value = [2,4][math.floor(random()*2)]
        else:
            self.value = 0

        if (value != 0):
            self.value = value

        if (value == 1):
            self.value = 0

        self.x = gridx
        self.y = gridy

        self.object = canvas.create_rectangle((size-border*1.25)/4*self.x+border,
                                               (size-border*1.25)/4*self.y+border+panelHeight,
                                               (size-border*1.25)/4*self.x+(size-border*1.25)/4,
                                               (size-border*1.25)/4*self.y+(size-border*1.25)/4+panelHeight,
                                                fill = '#bdc3c7' if self.value == 0 else colors[int(math.log(self.value,2)%len(colors))-1])
        self.text = canvas.create_text((size-border*1.25)/4*self.x+textPadding+border, (size-border*1.25)/4*self.y+textPadding+border+panelHeight, text=str(self.value) if self.value != 0 else "", width=(size-border*1.25)/4-2*textPadding, font = ("Arial", math.floor(textSize)))

    def draw(self):
        self.object = canvas.create_rectangle((size-border*1.25)/4*self.x+border,
                                              (size-border*1.25)/4*self.y+border+panelHeight,
                                              (size-border*1.25)/4*self.x+(size-border*1.25)/4,
                                              (size-border*1.25)/4*self.y+(size-border*1.25)/4+panelHeight,
                                                fill = '#bdc3c7' if self.value == 0 else colors[int(math.log(self.value,2)%len(colors))-1])
        self.text = canvas.create_text((size-border*1.25)/4*self.x+textPadding+border, (size-border*1.25)/4*self.y+textPadding+border+panelHeight, text=str(self.value) if self.value != 0 else "", width=(size-border*1.25)/4-2*textPadding, font = ("Arial", math.floor(textSize)))

    
DIRECTIONS = ["up", "down", "left", "right"]
size = 700 
border = 75
score = 0
hasContinued = False
msPF = 10
textSize = (size-border*1.25)/4/2
textPadding = textSize/2
panelHeight = size/12
colors = ["#f1c40f", "#e67e22", "#e74c3c", "#2ecc71", "#1abc9c", "#3498db", "#9b59b6"]

root = Tk()

canvas = Canvas(root, bg='light grey', height=size, width=size)
canvas.focus_set()
canvas.bind("<Key>", key)
canvas.pack()

newGame = Button(root, text ="New Game", command=restart, font=("Arial",20), width = int((size-2*(size-border*1.25)/4)/10+5))
newGameWindow = canvas.create_window((size-border*1.25)/8, (size-border*1.25)/64, anchor=NW, window=newGame)

scoreBg = canvas.create_rectangle((size-border*1.25)/8, (size-border*1.25)/16+5, 5+2*border+(math.floor((size-border*1.25)/16)*len("Score: " + str(score)))/2, (size-border*1.25)/16+2*math.floor((size-border*1.25)/16), fill = '#ecf0f1')
scoreObj = canvas.create_text((size-border*1.25)/8+5+border/2, (size-border*1.25)/16+math.floor((size-border*1.25)/16), text = "Score: " + str(score), font = ("Arial", math.floor((size-border*1.25)/16)), anchor=W)

firstTwo = [math.floor(random()*16) for i in range(2)]
while (firstTwo[0] == firstTwo[1]):
    firstTwo[1] = math.floor(random()*16)

grid = [[GridObject(i,j,0) for i in range(4)] for j in range(4)]

root.mainloop()
