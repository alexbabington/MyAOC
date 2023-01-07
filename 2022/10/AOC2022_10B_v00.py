#Advent of code 2022
#Day 10 Part 2
#Cathode-Ray Tube

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy
import math

start_time = time.time()

###Functions
def addx(instruction,x,cycle,screen):
    #Performs the addx instruction
    
    cycle += 1
    screen = draw_pixel_if_necessary(x,cycle,screen)
    
    cycle += 1
    x += instruction[1]
    screen = draw_pixel_if_necessary(x,cycle,screen)
    
    return x,cycle,screen

def draw_pixel_if_necessary(x,cycle,screen):
    #If the CRT and sprite position overlap a pixel is drawn
    row = math.floor(cycle/40)
    column = cycle - (row*40)
    
    if x-1 == column or x == column or x+1 == column: #Draw a pixel
        screen[row][column] = 1
    
    return screen

###Import and sort File
instructions = []

with open("input_10.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        if line == "noop":
            line = ["noop",0]
        else:
            line = line.split(" ")
            line[1] = int(line[1])
        
        instructions.append(line)

###Initial Conditions
x = 1
cycle = 0
screen = np.zeros([6,40],dtype=str)

###Main Code
screen = draw_pixel_if_necessary(x,cycle,screen)

for instruction in instructions:
    if instruction[0] == "addx":
        [x,cycle,screen] = addx(instruction,x,cycle,screen)
    elif instruction[0] == "noop":
        cycle += 1
        screen = draw_pixel_if_necessary(x,cycle,screen)
    else:
        print("This instruction is invalid")
        pdb.set_trace()

#replace 1 in screen with a block
for i,row in enumerate(screen):
    for k,pixel in enumerate(row):
        if pixel == "1":
            screen[i][k] = "█"
        else:
            screen[i][k] = " "

###Result
#print(instructions)
for el in screen:
     print(''.join(el.astype(str)))

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")