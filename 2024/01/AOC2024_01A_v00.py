#Advent of code 2024
#Day 1 Part 1
#Historian Hysteria

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
left = []
right = []
diff = []

with open("input_01.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = line.split("   ")#split on whitespace
        line = list(map(int,line))
        
        left.append(line[0])
        right.append(line[1])

left = sorted(left)
right = sorted(right)


###Initial Conditions
diff_sum = 0

###Main Code
for i,l in enumerate(left):
    r = right[i]
    diff = abs(r-l)
    #print(diff)
    diff_sum += diff


###Result
#print(left)
#print(right)
#print(diff)
print(diff_sum)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")