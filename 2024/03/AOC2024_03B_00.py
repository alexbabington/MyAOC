#Advent of code 2024
#Day 3 Part 2
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
        line = line.replace("do[]","")
        line = line.replace("do()","do[]")
        line = line.replace("don't[]","")
        line = line.replace("don't()","don't[]")
        line = line.split("(")
        
        
        
        input.append(line)

memories = input

###Initial Conditions
sum = 0
execute_bool = 1

###Main Code
for i_a,memory in enumerate(memories):
    for i_b,snippet in enumerate(memory):
        #print(i_b)
        
        if i_b <= 0:
            continue
        
        if execute_bool == 1:
            if snippet.count(")") > 0:
                instruction = snippet.split(")")
                instruction = instruction[0]
                
                if memory[i_b-1][-3:] == "mul":
                    #print("possible instruction detected")
                    #print(execute_bool)
                    #print("instruction is ",snippet)
                    instruction = instruction.split(",")
                    if len(instruction) == 2:
                        if instruction[0].isnumeric() & instruction[1].isnumeric():
                            #print("valid instruction")
                            #print(instruction)
                            sum += int(instruction[0])*int(instruction[1])
        
        #print(snippet)
        
        if snippet.count("do[]") > 0:
            execute_bool = 1
        if snippet.count("don't[]") > 0:
            execute_bool = 0


###Result
#print(input)
print(sum)
timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")