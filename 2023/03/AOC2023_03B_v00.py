#Advent of code 2023
#Day 3 Part 1
#Gear Ratios

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def identify_symbol(char):
    #Function takes a character and returns true if it is a symbol and false if it is not
    if char in "0123456789.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        bool = False
    else:
        bool = True
        
    return bool

def find_nearby_numbers(char,row,column,schematic):
    #Function to find and return any numbers which are nearby
    
    #print(char)
    #pdb.set_trace()
    
    numbers = []
    no_of_rows = np.shape(schematic)[0]
    no_of_columns = np.shape(schematic)[1]
    
    #up
    if row > 0:
        if column > 0:
            up_left = schematic[row-1][column-1]
            #print("Up Left is ",up_left)
        up_middle = schematic[row-1][column]
        #print("Up Middle is ",up_middle)
        if column + 1 < no_of_columns:
            up_right = schematic[row-1][column+1]
            #print("Up Right is ",up_right)
        #Deal with up row by checking middle first. If middle is a number send that for expansion. If not, check left and right.
        if up_middle.isnumeric() == True:
            numbers.append(expand_number(up_middle,row-1,column,schematic))
        else:
            if up_left.isnumeric() == True and column > 0:
                numbers.append(expand_number(up_left,row-1,column-1,schematic))
            if up_right.isnumeric() == True and column + 1 < no_of_columns:
                numbers.append(expand_number(up_right,row-1,column+1,schematic))
    
    #This row
    #Left
    if column > 0:
        left = schematic[row][column-1]
        #print("Left is ",left)
        if left.isnumeric() == True:
            numbers.append(expand_number(left,row,column-1,schematic))
    #Right
    if column + 1 < no_of_columns:
        right = schematic[row][column+1]
        #print("Right is ",right)
        if right.isnumeric() == True:
            numbers.append(expand_number(right,row,column+1,schematic))
    
    #Down
    if row + 1 < no_of_rows:
        if column > 0:
            down_left = schematic[row+1][column-1]
            #print("Down Left is ",down_left)
        down_middle = schematic[row+1][column]
        #print("Down Middle is ",down_middle)
        if column + 1 < no_of_columns:
            down_right = schematic[row+1][column+1]
            #print("Down Right is ",down_right)
        
        #Deal with down row by checking middle first. If middle is a number send that for expansion. If not, check left and right.
        if down_middle.isnumeric() == True:
            numbers.append(expand_number(down_middle,row+1,column,schematic))
        else:
            if down_left.isnumeric() == True and column > 0:
                numbers.append(expand_number(down_left,row+1,column-1,schematic))
            if down_right.isnumeric() == True and column + 1 < no_of_columns:
                numbers.append(expand_number(down_right,row+1,column+1,schematic))
    
    return numbers

def expand_number(char,row,column,schematic):
    #Takes a character found from a number and expands it by searching left and right
    
    no_of_rows = np.shape(schematic)[0]
    no_of_columns = np.shape(schematic)[1]
    
    number = char
    
    #Search Left
    continue_search = True
    col_new = column
    while continue_search == True:
        col_new -= 1
        if col_new >= 0:
            char_to_test = schematic[row][col_new]
            if char_to_test.isnumeric() == True:
                number = char_to_test + number
            else:
                continue_search = False
        else:
            continue_search = False
            
    #Search Right
    continue_search = True
    col_new = column
    while continue_search == True:
        col_new += 1
        if col_new + 1 <= no_of_columns:
            char_to_test = schematic[row][col_new]
            if char_to_test.isnumeric() == True:
                number = number + char_to_test
            else:
                continue_search = False
        else:
            continue_search = False
    
    number = int(number)
    
    return number




###Import and sort File
input = []

with open("input_03.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(line)
        
        input.append(line)

schematic = np.array(input,dtype=object)

#print(schematic)

###Initial Conditions
sum_of_part_numbers = 0
sum_of_gear_ratios = 0

###Main Code
for row,line in enumerate(schematic):#Iterate through each line
    for column,char in enumerate(line):#Iterate through each line
        if identify_symbol(char) == True:#If it is a symbol, find any numbers which are nearby
            numbers = find_nearby_numbers(char,row,column,schematic)
            
            for i_c,number in enumerate(numbers):
                sum_of_part_numbers += number
            
            if char == "*" and len(numbers) == 2:
                #print(numbers)
                sum_of_gear_ratios += numbers[0]*numbers[1]

###Result
print("Sum of part numbers is ",sum_of_part_numbers)
print("Sum of gear ratios is ",sum_of_gear_ratios)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")