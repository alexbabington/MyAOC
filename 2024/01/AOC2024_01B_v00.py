#Advent of code 2024
#Day 1 Part 2
#Historian Hysteria

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy
from collections import Counter

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
sum = 0

###Main Code
l_count = Counter(left)
r_count = Counter(right)

for i,value in enumerate(l_count):
    #print(value)
    l_num = l_count[value]
    r_num = r_count[value]
    sum += value * l_num * r_num


###Result
print(sum)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")