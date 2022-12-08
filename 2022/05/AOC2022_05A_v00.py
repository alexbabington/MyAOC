#Advent of code 2022
#Day 05 Part 1
#Supply Sacks

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Functions
def move_crates(movement,stacks):
    #Performs a single movement instruction
    move_no = movement[0]
    from_loc = movement[1]
    to_loc = movement[2]
    crates_to_relocate = stacks[from_loc][0:move_no]
    stacks[from_loc] = stacks[from_loc][move_no:len(stacks[from_loc])]
    for crate in crates_to_relocate:
        stacks[to_loc].insert(0,crate)
        
    return stacks

###Import and sort File
package_map = []#Each line of input from the package map copied exactly into a list entry with end markers removed
movements = []#a list of move instructions. For each list entry a sub list or 3 numbers which are: quantity to move, from location, to location

with open("input_05.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        if line[0:4] == "move":
            
            line = line.replace("move ","")
            line = line.replace("from","")
            line = line.replace("to","")
            line = line.split()
            line = list(map(int,line))
            line = [x - 1 for x in line]
            line[0] += 1
            movements.append(line)
        elif line != "":
            package_map.append(line)

#Sort package map into a top down list for each stack
no_stacks = int((len(package_map[len(package_map)-1]) + 1) / 4)
stacks = []
#Iteate through and populate each stack
i = 0#which stack we are on
ic = 1#which char in string that is located
while i < no_stacks:
    #Iterate through package_map and log any enteries
    stack = []
    for line in package_map:
        package = line[ic]
        if line[ic] == " ":
            continue
        elif line[ic].isnumeric():
            continue
        else:
            stack.append(package)
    
    stacks.append(stack)
    
    i += 1
    ic += 4

print(package_map)
print(stacks)
print(movements)

###Main Code
for movement in movements:
    stacks = move_crates(movement,stacks)

#List crates on top
top = ""
for stack in stacks:
    top += stack[0]

#Result
print(stacks)
print(top)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")