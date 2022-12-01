#Advent of code 2022
#Day 01 Part 1
#Calorie Counting

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

#Functions
def function(inputs):
    
    return output

#Import and sort File
elfs = []
elf = []

with open("input_01.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        if line == "":
            elfs.append(elf)
            elf = []
        else:
            line = int(line)
            elf.append(line)

elfs.append(elf)

###Main Code
#Find total calories carried by wach elf
elfs_sum = []
for i, elf in enumerate(elfs):
    total_cal = sum(elf)
    elfs_sum.append(total_cal)

max_cal = max(elfs_sum)

#Result
print(max_cal)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")