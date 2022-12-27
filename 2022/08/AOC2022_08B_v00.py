#Advent of code 2022
#Day 08 Part 2
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

def find_shit_i_can_see_score(map,i,k):
    #Takes a map of trees and the position of a tree to evaluate and returns a score for what it can see
    tree = map[i][k]
    left_of_tree = map[i][0:k]
    left_of_tree = np.flip(left_of_tree)
    left_visible = find_no_visible_in_a_direction(left_of_tree,tree)
    
    right_of_tree = map[i][k+1:]
    right_visible = find_no_visible_in_a_direction(right_of_tree,tree)
    
    north_of_tree = map[:,k][0:i]
    north_of_tree = np.flip(north_of_tree)
    north_visible = find_no_visible_in_a_direction(north_of_tree,tree)
    
    south_of_tree = map[:,k][i+1:]
    south_visible = find_no_visible_in_a_direction(south_of_tree,tree)
    
    shit_i_can_see_score = left_visible * right_visible * north_visible * south_visible
    
    #print(map)
    #print(tree)
    #print(north_visible)
    #print(right_visible)
    #print(south_visible)
    #print(left_visible)
    #pdb.set_trace()
    
    return shit_i_can_see_score

def find_no_visible_in_a_direction(trees_in_direction,tree):
    ### Finds how many are visible in a directions
    no_visible = 0#Initialise at 0 and add any visible trees found
    for test_tree in trees_in_direction:
        if test_tree < tree:
            no_visible += 1
        elif test_tree == tree:
            no_visible += 1
            break
        else:
            no_visible += 1
            break
    
    return no_visible

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
tree_visibility_scores =[]
for i,row in enumerate(map):
    for k, tree in enumerate(row):
        print(i," , ",k)
        #Calculate tree visability score
        shit_i_can_see_score = find_shit_i_can_see_score(map,i,k)
        tree_visibility_scores.append(shit_i_can_see_score)

max_visibility = max(tree_visibility_scores)

#Result
print(map)
print(tree_visibility_scores)
print(max_visibility)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")