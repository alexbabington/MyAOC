#Advent of code 2024
#Day 3 Part 1
#Mull It Over

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

with open("input_03.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        #line = line.replace(")","(")
        line = line.split("(")
        
        
        
        input.append(line)

memories = input

###Initial Conditions
sum = 0

###Main Code
for i_a,memory in enumerate(memories):
    for i_b,snippet in enumerate(memory):
        #print(i_b)
        if i_b <= 0:
            continue
        
        if snippet.count(")") == 0:
            continue
        
        
        snippet = snippet.split(")")
        snippet = snippet[0]
        
        if memory[i_b-1][-3:] == "mul":
            #print("possible instruction detected")
            #print("instruction is ",snippet)
            instruction = snippet.split(",")
            if len(instruction) == 2:
                if instruction[0].isnumeric() & instruction[1].isnumeric():
                    #print("valid instruction")
                    #print(instruction)
                    sum += int(instruction[0])*int(instruction[1])


###Result
#print(input)
print(sum)
timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")