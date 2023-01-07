#Advent of code 2022
#Day 10 Part 1
#Cathode-Ray Tube

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Functions
def addx(instruction,x,cycle,list_of_interesting_signal_strengths):
    
    cycle += 1
    list_of_interesting_signal_strengths = is_this_cycle_interesting(list_of_interesting_signal_strengths, list_of_interesting_cycles, cycle, x)
    
    cycle += 1
    list_of_interesting_signal_strengths = is_this_cycle_interesting(list_of_interesting_signal_strengths, list_of_interesting_cycles, cycle, x)
    x += instruction[1]
    
    return x,cycle,list_of_interesting_signal_strengths

def is_this_cycle_interesting(list_of_interesting_signal_strengths, list_of_interesting_cycles, cycle, x):
    
    if cycle in list_of_interesting_cycles:
        signal_strength = x * cycle
        list_of_interesting_signal_strengths.append(signal_strength)
    
    return list_of_interesting_signal_strengths

###Import and sort File
instructions = []

with open("input_10.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        if line == "noop":
            line = ["noop",0]
        else:
            line = line.split(" ")
            line[1] = int(line[1])
        
        instructions.append(line)

###Initial Conditions
x = 1
cycle = 0
list_of_interesting_cycles = [20,60,100,140,180,220]
list_of_interesting_signal_strengths = []

###Main Code
for instruction in instructions:
    if instruction[0] == "addx":
        [x,cycle,list_of_interesting_signal_strengths] = addx(instruction,x,cycle,list_of_interesting_signal_strengths)
    elif instruction[0] == "noop":
        cycle += 1
        list_of_interesting_signal_strengths = is_this_cycle_interesting(list_of_interesting_signal_strengths, list_of_interesting_cycles, cycle, x)
    else:
        print("This instruction is invalid")
        pdb.set_trace()

sum_of_signal_strengths = sum(list_of_interesting_signal_strengths)

###Result
#print(instructions)
#print(list_of_interesting_signal_strengths)
print(sum_of_signal_strengths)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")