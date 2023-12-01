#Advent of code 2023
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

with open("input_01.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        input.append(line)

input = np.array(input,dtype=object)

###Initial Conditions

###Main Code
calibration_values = []
for i,line in enumerate(input):
    #Get Calibration Values
    digits = []
    for k,char in enumerate(line):
        #Iterate through each character
        if char.isdigit():
            digits.append(char)
    calibration_value = int(digits[0] + digits[-1])
    calibration_values.append(calibration_value)

result = sum(calibration_values)

###Result
print(result)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")