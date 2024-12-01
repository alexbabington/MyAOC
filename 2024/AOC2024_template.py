#Advent of code 2024
#Day 1 Part 1
#Trebuchet?

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
#def function(inputs):
#    #Function
#
#    return outputs

###Import and sort File
input = []

with open("input_##_test.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        
        
        input.append(line)

input = np.array(input,dtype=object)

###Initial Conditions

###Main Code

###Result
print(input)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")