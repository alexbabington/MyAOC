#Advent of code 2024
#Day 8 Part 2
#Resonant Collinearity

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy
from itertools import combinations

start_time = time.time()

###Constants

###Functions
#def function(inputs):
#    #Function
#
#    return outputs

###Import and sort File
input = []

with open("input_08.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        
        
        input.append(line)

map = input
#print(map)

no_rows = len(map)
no_columns = len(map[0])

print("Size is ",no_rows," rows by ",no_columns," columns")

###Initial Conditions
antinode_map = np.zeros([no_rows,no_columns])
#print(antinode)
f_coord_dict = {}

###Main Code
#Iterate through, find list of co-ordinates for each unique frequency
for i_row,row in enumerate(map):
    for i_col,tower in enumerate(row):
        if tower != ".":
            #Contains an antenna
            coord = [i_row,i_col]
            if tower in f_coord_dict:
                coord_list = f_coord_dict[tower]
                coord_list.append(coord)
                f_coord_dict[tower] = coord_list
            else:
                f_coord_dict[tower] = [coord]

#print("Dictionary of coordinates is ",f_coord_dict)

#For each seperate tower frequency generate list of all tower pair combinations
#Generate antinodes
#Insert Antinodes to antinode map if valid
for i_t,tower in enumerate(f_coord_dict):
    #print("Tower frequency is ",tower)
    coord_list = f_coord_dict[tower]
    coord_pairs_list = list(combinations(coord_list,2))
    #print("Coord pairs list is ",coord_pairs_list)
    
    #Iterate through co-ord pair list and generate list of possible anti-node co-ordinates
    #Insert antinodes to antinode map if valid
    for i_cp,coord_pair in enumerate(coord_pairs_list):
        #print("coord pair is ",coord_pair)
        
        xs = [coord_pair[0][0],coord_pair[1][0]]
        ys = [coord_pair[0][1],coord_pair[1][1]]
        
        diff_x = xs[1] - xs[0]
        diff_y = ys[1] - ys[0]
        
        i_d = 0
        out_of_bounds = False
        while out_of_bounds == False:
            anti_x = xs[0] - (diff_x*i_d)
            anti_y = ys[0] - (diff_y*i_d)
            
            if anti_x >= 0 and anti_x < no_rows and anti_y >= 0 and anti_y < no_rows:
                #Antinode is valid
                antinode_map[anti_x][anti_y] = 1
                
                i_d += 1
            
            else:
                out_of_bounds = True
        
        i_d = 0
        out_of_bounds = False
        while out_of_bounds == False:
            anti_x = xs[0] + (diff_x*i_d)
            anti_y = ys[0] + (diff_y*i_d)
            
            if anti_x >= 0 and anti_x < no_rows and anti_y >= 0 and anti_y < no_rows:
                #Antinode is valid
                antinode_map[anti_x][anti_y] = 1
                
                i_d += 1
            
            else:
                out_of_bounds = True
        
        #print("Xs are ",xs)
        #print("Ys are ",ys)
        
        #antinode_xs = [xs[0]-(xs[1]-xs[0]),xs[1]+(xs[1]-xs[0])]
        #antinode_ys = [ys[0]-(ys[1]-ys[0]),ys[1]+(ys[1]-ys[0])]
        
        #print("Antinode Xs are ",antinode_xs)
        #print("Antinode Ys are ",antinode_ys)
        
        #antinode_A = [antinode_xs[0],antinode_ys[0]]
        #antinode_B = [antinode_xs[1],antinode_ys[1]]
        #antinodes = [antinode_A,antinode_B]
        
        #print("Possible antinodes are ",antinodes)
        
        #If antinode is valid, then add antinode to antinode map:
        #if antinode_xs[0] >= 0 and antinode_xs[0] < no_rows and antinode_ys[0] >= 0 and antinode_ys[0] < no_columns:
        #    #Antinode is valid
        #    antinode_map[antinode_xs[0]][antinode_ys[0]] = 1
        #if antinode_xs[1] >= 0 and antinode_xs[1] < no_rows and antinode_ys[1] >= 0 and antinode_ys[1] < no_columns:
        #    #Antinode is valid
        #    antinode_map[antinode_xs[1]][antinode_ys[1]] = 1

#print(antinode_map)

###Result
unique_locations = sum(sum(antinode_map))
print("The number of unique antinodes is ",unique_locations)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")