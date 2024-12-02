#Advent of code 2024
#Day 2 Part 1
#Red-Nosed Reports

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def eval_slope(report):
    #Function to evaluate if all increasing or not
    #Returns -1 if all decreasing
    #Returns 0 if mixed
    #Returns 1 if all increasing
    slope = []
    
    for i_b,level in enumerate(report):
        if i_b == 0:
            continue
        else:
            slope.append(level - report[i_b-1])
            
    slope = np.array(slope,dtype=object)
    
    #print("Slopes are ",slope)
    
    if max(slope) <= 3 and min(slope) >= 1:
        overall_slope = 1
    elif max(slope) <= -1 and min(slope) >= -3:
        overall_slope = -1
    else:
        overall_slope = 0
    
    #print(overall_slope)
    
    return overall_slope

###Import and sort File
input = []

with open("input_02.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = line.split(" ")#Split on space
        line = list(map(int,line))
        
        
        
        input.append(line)

input = np.array(input,dtype=object)
reports = input

###Initial Conditions
safe = 0

###Main Code
for i_a,report in enumerate(reports):
    overall_slope = eval_slope(report)
    safe += abs(overall_slope)


###Result
print(safe)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")