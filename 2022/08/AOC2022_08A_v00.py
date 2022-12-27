#Advent of code 2022
#Day 08 Part 1
#Treetop Tree House

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

#Functions
def is_this_tree_pointy(map,i,k):
    #Takes a map of trees and the position of a tree to evaluate and returns if it is pointy
    tree = map[i][k]
    left_of_tree = map[i][0:k]
    right_of_tree = map[i][k+1:]
    north_of_tree = map[:,k][0:i]
    south_of_tree = map[:,k][i+1:]
    
    #Check if trees are equal or taller
    if max(left_of_tree) < tree or max(right_of_tree) < tree or max(north_of_tree) < tree or max(south_of_tree) < tree:
        pointy_bool = True
    else:
        pointy_bool = False
    
    return pointy_bool

def is_this_tree_at_the_edge(map,i,k):
    #Find Array Size
    shape = np.shape(map)
    no_rows = shape[0]
    no_colums = shape[1]    
    
    #Takes a map of trees and the position of a tree to evaluate and returns if it is pointy
    if i == 0  or k == 0:
        #It is at the left or top of the map
        edgey_bool = True
    elif i == no_rows - 1 or k == no_colums - 1:
        #It is at the end of the map
        edgey_bool = True
    else:
        edgey_bool = False
    
    return edgey_bool

#Import and sort File
map = []

with open("input_08.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        line = list(line)
        line = [int(x) for x in line]
        
        map.append(line)

map = np.array(map)

###Main Code
#Iterate over array and evalualte if each tree sticks out above other trees
pointy_counter = 0
for i,row in enumerate(map):
    for k, tree in enumerate(row):
        #Check if this is a tree at the edge of the map and if so mark it is pointy
        edgey_bool = is_this_tree_at_the_edge(map,i,k)
        if edgey_bool == True:
            pointy_bool = True
            pointy_counter += 1
            continue
        
        #Check if this tree is pointy
        pointy_bool = is_this_tree_pointy(map,i,k)
        if pointy_bool == True:
            pointy_counter += 1
            continue

#Result
print(map)
print(pointy_counter)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")