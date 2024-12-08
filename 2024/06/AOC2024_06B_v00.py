#Advent of code 2024
#Day 6 Part 2
#Guard Gallivant

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def find_next_coord(guard):
    #Returns co-ordinate in front of the guard
    
    row = guard[0]
    column = guard[1]
    direction = guard[2]
    
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "right":
        column += 1
    elif direction == "left":
        column -= 1
    else:
        print("ERROR!!!: direction of the guard is not valid")
        pdb.set_trace()
    
    next_coord = [row, column]
    
    return next_coord

def rotate(guard):
    #Rotates the guard 90 degrees to the right
    direction = guard[2]
    
    if direction == "up":
        direction = "right"
    elif direction == "down":
        direction = "left"
    elif direction == "right":
        direction = "down"
    elif direction == "left":
        direction = "up"
    else:
        print("ERROR!!!: direction of the guard is not valid")
        pdb.set_trace()
    
    guard[2] = direction
    
    return guard

def run_guard_pathing(guard,map):
    distinct_pos = 1
    i = 0
    out_of_bounds = False
    while out_of_bounds == False and i < 10000:
        #Find next co-ord if guard moved forward
        next_coord = find_next_coord(guard)
        
        #Stop if out of bounds
        row = next_coord[0]
        column = next_coord[1]
        if row < 0 or column < 0 or row > map_no_rows or column > map_no_columns:
            out_of_bounds = True
        
        #If next co-ord is blocked, rotate guard
        elif map[next_coord[0]][next_coord[1]] == "#":
            guard = rotate(guard)
        
        #else advance guard
        else:
            #If next coord is unvisited mark as visited
            if map[next_coord[0]][next_coord[1]] == ".":
                map[next_coord[0]][next_coord[1]] = "X"
                distinct_pos += 1
            
            #Advance Guard
            guard = [next_coord[0],next_coord[1],guard[2]]
        
        i += 1
        
        if out_of_bounds == True:
            loop_bool = False
        else:
            loop_bool = True
        
    return loop_bool

def remove_duplicates(old_list):
    
    new_list = []
    
    for item in old_list:
        if item in new_list:
            continue
        else:
            new_list.append(item)
    
    return new_list

###Import and sort File
input = []

with open("input_06.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        input.append(line)

input = np.array(input,dtype=object)
map = input
#print("Staring map is ")
#print(map)

###Initial Conditions
distinct_pos = 1
out_of_bounds = False
map_no_rows = len(map) - 1
map_no_columns =  len(map[0]) - 1
pos_obstructions = []
no_loops = 0

###Main Code
#Find staring co-ordinates of the guard
start_coord = np.argwhere(map=="^")[0]
map[start_coord[0]][start_coord[1]] = "X"
#print("Guard starts point upwards at ",start_coord)

#Guard position and direction
guard = [start_coord[0],start_coord[1],"up"]
#print("Guard position and direction is ",guard)

tmpmap = copy.deepcopy(map)

while out_of_bounds == False:
    #Find next co-ord if guard moved forward
    next_coord = find_next_coord(guard)
    
    #Stop if out of bounds
    row = next_coord[0]
    column = next_coord[1]
    if row < 0 or column < 0 or row > map_no_rows or column > map_no_columns:
        out_of_bounds = True
    
    #If next co-ord is blocked, rotate guard
    elif tmpmap[next_coord[0]][next_coord[1]] == "#":
        guard = rotate(guard)
    
    #else advance guard
    else:
        #If next coord is unvisited mark as visited
        if tmpmap[next_coord[0]][next_coord[1]] == ".":
            tmpmap[next_coord[0]][next_coord[1]] = "X"
            distinct_pos += 1
        #If next coord visited count as obsctruciton
        if tmpmap[next_coord[0]][next_coord[1]] == "X":
            pos_obstructions.append(next_coord)
        
        #Advance Guard
        guard = [next_coord[0],next_coord[1],guard[2]]

#print("possible obstructions are ")
#print(pos_obstructions)

#Remvoe duplicates
pos_obstructions = remove_duplicates(pos_obstructions)

#print("possible obstructions are ")
#print(pos_obstructions)

#Check each obstructions
for i_a,obstruction in enumerate(pos_obstructions):
    guard = [start_coord[0],start_coord[1],"up"]
    
    
    tmpmap = copy.deepcopy(map)
    tmpmap[obstruction[0]][obstruction[1]] = "#"
    
    #print("Temp map is ")
    #print(tmpmap)
    
    loop_bool = run_guard_pathing(guard,tmpmap)
    
    if loop_bool == True:
        #print("Obstruction detected at ",obstruction)
        no_loops += 1



###Result
print("The number of obstructions causing loops is ",no_loops)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")