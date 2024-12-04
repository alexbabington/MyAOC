#Advent of code 2024
#Day 4 Part 1
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
#def function(inputs):
#    #Function
#
#    return outputs

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
max_x = len(map)-4
max_y = len(map[0])-4

for x,line in enumerate(map):
    for y,char in enumerate(line):
        if char == "X":
            #print("'X' located at co-ordinate ",x,",",y)
            #Check surrounding areas for 'MAS'
            #Check Up
            if x >= 3:
                up = map[x-1][y] + map[x-2][y] + map[x-3][y]
                if up == "MAS":
                    #print("Upwards 'XMAS' found")
                    no_xmas += 1
            #Check Down
            if x <= max_x:
                down = map[x+1][y] + map[x+2][y] + map[x+3][y]
                if down == "MAS":
                    #print("Downwards 'XMAS' found")
                    no_xmas += 1
            #Check Left
            if y >= 3:
                left = map[x][y-1] + map[x][y-2] + map[x][y-3]
                if left == "MAS":
                    #print("Leftwards 'XMAS' found")
                    no_xmas += 1
            #Check Right
            if y <= max_y:
                right = map[x][y+1] + map[x][y+2] + map[x][y+3]
                if right == "MAS":
                    #print("Rightwards 'XMAS' found")
                    no_xmas += 1
            #Check Up Left
            if x >= 3 and y >= 3:
                upleft = map[x-1][y-1] + map[x-2][y-2] + map[x-3][y-3]
                if upleft == "MAS":
                    #print("Up-Left-wards 'XMAS' found")
                    no_xmas += 1
            #Check Up Right
            if x >= 3 and y <= max_y:
                upright = map[x-1][y+1] + map[x-2][y+2] + map[x-3][y+3]
                if upright == "MAS":
                    #print("Up-Right-wards 'XMAS' found")
                    no_xmas += 1
            #Check Down Left
            if x <= max_x and y >= 3:
                downleft = map[x+1][y-1] + map[x+2][y-2] + map[x+3][y-3]
                if downleft == "MAS":
                    #print("Down-Left-wards 'XMAS' found")
                    no_xmas += 1
            #Check Down Right
            if x <= max_x and y <= max_y:
                downright = map[x+1][y+1] + map[x+2][y+2] + map[x+3][y+3]
                if downright == "MAS":
                    #print("Down-Right-wards 'XMAS' found")
                    no_xmas += 1

###Result
#print(input)
print("Number of ocurances of xmas found is ",no_xmas)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")