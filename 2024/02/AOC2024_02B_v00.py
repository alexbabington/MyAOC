#Advent of code 2024
#Day 2 Part 2
#Red-Nosed Reports

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def eval_slope(report):
    #Function to evaluate if all increasing or not
    #Returns -1 if all decreasing
    #Returns 0 if mixed
    #Returns 1 if all increasing
    slope = []
    
    for i_b,level in enumerate(report):
        if i_b == 0:
            continue
        else:
            slope.append(level - report[i_b-1])
            
    slope = np.array(slope,dtype=object)
    
    #print("Slopes are ",slope)
    
    up = sum((slope >= 1) & (slope <= 3))
    down = sum((slope >= -3) & (slope <= -1))
    zero = sum(slope == 0)
    
    #print("Up is ",up)
    #print("Down is ",down)
    #print("zero is ",zero)
    
    overall_slope = 0
    overall_slope += max(up,down)
    
    #if (up+down+zero) != len(slope):
    #    overall_slope = 0
    
    #("Overall slope is ",overall_slope)
    
    return overall_slope, slope

###Import and sort File
input = []

with open("input_02.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = line.split(" ")#Split on space
        line = list(map(int,line))
        
        
        
        input.append(line)

input = np.array(input,dtype=object)
reports = input

###Initial Conditions
safe = 0

###Main Code
for i_a,report in enumerate(reports):
    [overall_slope,slope] = eval_slope(report)
    if overall_slope == (len(report) - 1):
        safe += 1
    #elif overall_slope == (len(report) - 2):
    elif 1 > 0:
        #Problem Damper
        #print("apply problem damper")
        #print("report is ",report)
        
        safechk = 0
        
        for i_c,level in enumerate(report):
            #Remove each level
            report_short = np.delete(report,i_c)
            #print("report short is ",report_short)
            
            #Test new report
            [overall_slope,slope] = eval_slope(report_short)
            if overall_slope == (len(report_short) - 1):
                safe += 1
                safechk = 1
                #print("marked as safe")
                break
        
        #if safechk == 0:
            #print("!!! marked as not safe !!!")


###Result
print("Number safe is ",safe)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")