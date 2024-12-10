#Advent of code 2024
#Day 7 Part 2
#Bridge Repair

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

with open("input_07.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = line.split(": ")
        line[0] = int(line[0])
        line[1] = line[1].split(" ")
        line[1] = list(map(int,line[1]))
        
        input.append(line)

calibrations = input

#print(calibrations)

###Initial Conditions
sum_valid = 0

###Main Code
#Iterate for each calibration
for i_a,calibration in enumerate(calibrations):
    test = calibration[0]
    operators = calibration[1]
    #print("Test value is ",test)
    #print("Operators are ",operators)
    
    #Iterate through operators and find all possible sums
    for i_b,operator in enumerate(operators):
        if i_b == 0:
            sums = [operator]
            continue
        
        sums_old = copy.deepcopy(sums)
        sums = []
        
        for i_c,sum in enumerate(sums_old):
            #multiplication
            sums.append(sum * operator)
            #Addition
            sums.append(sum + operator)
            #Concatenation
            sums.append(int(str(sum)+str(operator)))
    
    #print("Possible sums are ",sums)
    
    #Enact if test value in list
    if test in sums:
        sum_valid += test

###Result
print("The sum of the valid calibration test values is ",sum_valid)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")