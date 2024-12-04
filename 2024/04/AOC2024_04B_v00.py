#Advent of code 2024
#Day 4 Part 2
#Ceres Search

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def contains(search,string):
    #Returns true if all char in string
    bool = False
    count = 0
    
    for i,char in enumerate(search):
        if char in search:
            count += 1
    
    if count == len(search):
        bool = True
    
    return bool

###Import and sort File
input = []

with open("input_04.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        
        
        input.append(line)

input = np.array(input,dtype=object)
map = input

###Initial Conditions
no_xmas = 0

###Main Code
#Get array size
max_x = len(map)-2
max_y = len(map[0])-2

for x,line in enumerate(map):
    for y,char in enumerate(line):
        if char == "A" and x >= 1 and y >= 1 and x <= max_x and y <= max_y:
            #print("'A' located at co-ordinate ",x,",",y)
            #Get Diagonal down-right
            downright = map[x-1][y-1] + map[x][y] + map[x+1][y+1]
            #print(downright)
            #Get Diagonal up-right
            upright = map[x-1][y+1] + map[x][y] + map[x+1][y-1]
            #print(upright)
            
            if (downright == "MAS" or downright == "SAM") and (upright == "MAS" or upright == "SAM"):
                #print("X-MAS found")
                no_xmas+=1

###Result
#print(input)
print("Number of ocurances of xmas found is ",no_xmas)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")