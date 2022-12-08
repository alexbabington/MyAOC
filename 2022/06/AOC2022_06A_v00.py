#Advent of code 2022
#Day 06 Part 1
#Turning Trouble

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
with open("input_06.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        #line = line.split(" -> ")
        
        datastream = line

###Main Code
for i,char in enumerate(datastream):
    possible_packet_marker = datastream[i:i+4]
    if len(possible_packet_marker) == len(set(possible_packet_marker)):
        #This is a start-of-packet market
        break

#Result
print(datastream)
print(i+4)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")