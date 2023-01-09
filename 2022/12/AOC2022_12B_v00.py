#Advent of code 2022
#Day 12 Part 1
#Hill Climbing Algorithm

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants
height_letter2num = {}
height_letter2num["a"] = 0
height_letter2num["b"] = 1
height_letter2num["c"] = 2
height_letter2num["d"] = 3
height_letter2num["e"] = 4
height_letter2num["f"] = 5
height_letter2num["g"] = 6
height_letter2num["h"] = 7
height_letter2num["i"] = 8
height_letter2num["j"] = 9
height_letter2num["k"] = 10
height_letter2num["l"] = 11
height_letter2num["m"] = 12
height_letter2num["n"] = 13
height_letter2num["o"] = 14
height_letter2num["p"] = 15
height_letter2num["q"] = 16
height_letter2num["r"] = 17
height_letter2num["s"] = 18
height_letter2num["t"] = 19
height_letter2num["u"] = 20
height_letter2num["v"] = 21
height_letter2num["w"] = 22
height_letter2num["x"] = 23
height_letter2num["y"] = 24
height_letter2num["z"] = 25
height_letter2num["S"] = 0
height_letter2num["E"] = 25

###Functions
def update_if_paths_around_current_point_are_shorter(i,k,heightmap,distancemap,map_shape,no_updates):
    #Checks if any of the surrounding squares offer a shorter path with an allowed step height
    #If they do the distance to this point is changed to reflect the new path
    
    height = heightmap[i][k]
    distance = distancemap[i][k]
    
    new_distances = [distance]
    
    #Checks Above
    if i > 0:
        height_above = heightmap[i-1][k]
        distance_above = distancemap[i-1][k]
        if check_if_path_pair_is_shorter_and_valid(height,distance,height_above,distance_above):
            new_distances.append(distance_above + 1)
    #Checks Left
    if k > 0:
        height_left = heightmap[i][k-1]
        distance_left = distancemap[i][k-1]
        if check_if_path_pair_is_shorter_and_valid(height,distance,height_left,distance_left):
            new_distances.append(distance_left + 1)
    #Checks Below
    if i < map_shape[0]-1:
        height_below = heightmap[i+1][k]
        distance_below = distancemap[i+1][k]
        if check_if_path_pair_is_shorter_and_valid(height,distance,height_below,distance_below):
            new_distances.append(distance_below + 1)
    #Checks Right
    if k < map_shape[1]-1:
        height_right = heightmap[i][k+1]
        distance_right = distancemap[i][k+1]
        if check_if_path_pair_is_shorter_and_valid(height,distance,height_right,distance_right):
            new_distances.append(distance_right + 1)
    
    #Sets new distance to smallest distance option
    if min(new_distances) < distance:
        distancemap[i][k] = min(new_distances)
        no_updates += 1
    
    return heightmap,distancemap,no_updates

def check_if_path_pair_is_shorter_and_valid(height,distance,height_tocheck,distance_tocheck):
    
    if height - height_tocheck <= 1 and distance > distance_tocheck + 1:
        bool = True
    else:
        bool = False
    
    return bool

def find_shortest_path_length(heightmap,start_pos,end_pos):
    
    map_shape = np.shape(heightmap)
    distancemap = np.zeros(map_shape,dtype=int) + (26*2*map_shape[0]*map_shape[1])#Record shortest distance found to current square from the start
    distancemap[start_pos[0]][start_pos[1]] = 0
    
    no_updates = 1
    
    while no_updates > 0:#Iterate whilst changes are still being made
        no_updates = 0
        for i,row in enumerate(heightmap):
            for k,height in enumerate(row):
                [heightmap,distancemap,no_updates] = update_if_paths_around_current_point_are_shorter(i,k,heightmap,distancemap,map_shape,no_updates)
    
    shortest_path = distancemap[end_pos[0]][end_pos[1]]
    
    return shortest_path


###Import and sort File
heightmap = []

with open("input_12.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        for k,point in enumerate(line):
            line[k] = height_letter2num[point]
            
            if point == "S":
                start_pos = [i,k]
            
            if point == "E":
                end_pos = [i,k]
        
        heightmap.append(line)

heightmap = np.array(heightmap)

###Initial Conditions

###Main Code
#Find list of start positions
list_start_pos = []
for i,row in enumerate(heightmap):
    for k,height in enumerate(row):
        if height == 0:
            start_pos = [i,k]
            list_start_pos.append(start_pos)
print("Total possible start positions searched ",len(list_start_pos))

#Find shortest path from each start position
list_of_shortest_paths = []
for i,start_pos in enumerate(list_start_pos):
    print("Start positions searched ",i)
    shortest_path = find_shortest_path_length(heightmap,start_pos,end_pos)
    list_of_shortest_paths.append(shortest_path)

overall_shortest_path = min(list_of_shortest_paths)

###Result
#rint(heightmap)
#print(start_pos)
#print(end_pos)
#print(distancemap)
print(list_start_pos)
print(list_of_shortest_paths)
print("The shortest distance is ",overall_shortest_path)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")