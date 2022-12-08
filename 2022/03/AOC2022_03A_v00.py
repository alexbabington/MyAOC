#Advent of code 2022
#Day 03 Part 1
#Rucksack Reorganization

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

#Definitions
#Item Priority Scores
find_priority = {}
find_priority["a"] = 1
find_priority["b"] = 2
find_priority["c"] = 3
find_priority["d"] = 4
find_priority["e"] = 5
find_priority["f"] = 6
find_priority["g"] = 7
find_priority["h"] = 8
find_priority["i"] = 9
find_priority["j"] = 10
find_priority["k"] = 11
find_priority["l"] = 12
find_priority["m"] = 13
find_priority["n"] = 14
find_priority["o"] = 15
find_priority["p"] = 16
find_priority["q"] = 17
find_priority["r"] = 18
find_priority["s"] = 19
find_priority["t"] = 20
find_priority["u"] = 21
find_priority["v"] = 22
find_priority["w"] = 23
find_priority["x"] = 24
find_priority["y"] = 25
find_priority["z"] = 26
find_priority["A"] = 1 + 26
find_priority["B"] = 2 + 26
find_priority["C"] = 3 + 26
find_priority["D"] = 4 + 26
find_priority["E"] = 5 + 26
find_priority["F"] = 6 + 26
find_priority["G"] = 7 + 26
find_priority["H"] = 8 + 26
find_priority["I"] = 9 + 26
find_priority["J"] = 10 + 26
find_priority["K"] = 11 + 26
find_priority["L"] = 12 + 26
find_priority["M"] = 13 + 26
find_priority["N"] = 14 + 26
find_priority["O"] = 15 + 26
find_priority["P"] = 16 + 26
find_priority["Q"] = 17 + 26
find_priority["R"] = 18 + 26
find_priority["S"] = 19 + 26
find_priority["T"] = 20 + 26
find_priority["U"] = 21 + 26
find_priority["V"] = 22 + 26
find_priority["W"] = 23 + 26
find_priority["X"] = 24 + 26
find_priority["Y"] = 25 + 26
find_priority["Z"] = 26 + 26

#Functions
def function(inputs):
    
    return output

#Import and sort File
rucksacks = []

with open("input_03.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        if line != "":
            leng = len(line)
            half_leng = int(leng/2)
            line = [line[0:half_leng],line[half_leng:leng]]
        
            rucksacks.append(line)

###Main Code
total = 0

for i,rucksack in enumerate(rucksacks):
    common_chars = list(set(rucksack[0])&set(rucksack[1]))
    for char in common_chars:
        priority = find_priority[char]
        total += priority
    

#Result
print(total)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")