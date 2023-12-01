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
def num2digit(string):
    #Function
    string = string.replace("1ight","18")
    string = string.replace("2ne","21")
    string = string.replace("3ight","38")
    string = string.replace("5ight","58")
    string = string.replace("8wo","82")
    string = string.replace("9ight","98")
    
    string = string.replace("one","1")
    string = string.replace("two","2")
    string = string.replace("three","3")
    string = string.replace("four","4")
    string = string.replace("five","5")
    string = string.replace("six","6")
    string = string.replace("seven","7")
    string = string.replace("eight","8")
    string = string.replace("nine","9")
    return string

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
    string = ""
    for k,char in enumerate(line):
        #Iterate through each character
        string = string + char
        string = num2digit(string)
        if string[-1].isdigit():
            digits.append(string[-1])
    calibration_value = int(digits[0] + digits[-1])
    calibration_values.append(calibration_value)
    print("".join(line))
    #print(string)
    print(digits)
    #print(calibration_value)
    #pdb.set_trace()

result = sum(calibration_values)

###Result
print(result)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")