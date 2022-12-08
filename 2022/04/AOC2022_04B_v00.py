#Advent of code 2022
#Day 04 Part 2
#Camp Cleanup

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
pairs = []

with open("input_04.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        line = line.split(",")
        
        pair = []
        for ass_range in line:
            ass_limits = ass_range.split("-")
            assignment = []
            i = int(ass_limits[0])
            while i <= int(ass_limits[1]):
                assignment.append(i)
                i += 1
            pair.append(assignment)
        
        pairs.append(pair)

###Main Code
count = 0
#Evaluate each pair
for pair in pairs:
    overlap = list(set(pair[0])&set(pair[1]))
    len_overlap = len(overlap)
    if len_overlap > 0:
        count += 1

#Result
print(count)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")