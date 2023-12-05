#Advent of code 2023
#Day 5 Part 1
#If You Give A Seed A Fertilizer

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def convert_A_to_B(value,conversion_table):
    #Takes a value to convert and a converstion table in the format (destination, source, range). If value is not in range returns the original value
    
    for i_e,conversion in enumerate(conversion_table):#Evaluates value against each conversion
        start = conversion[1]
        end = conversion[1] + conversion[2]
        movement = conversion[0] - conversion[1]
        if value >= start and value <= end:
            value += movement
            break
    
    
    
    return value

###Import and sort File
seeds = []
seed2soil = []
soil2fertilizer = []
fertilizer2water = []
water2light = []
light2temp = []
temp2humidity = []
humidity2location = []

import_mode = ""

with open("input_05.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        if line == "":#Reset once section is read
            import_mode = ""
        elif line[0:6] == "seeds:" or import_mode == "seeds":
            import_mode = "seeds"
            line = line[7:].split()
            for i_a,seed in enumerate(line):
                seeds.append(int(seed))
        elif line == "seed-to-soil map:":
            import_mode = "seed2soil"
        elif import_mode == "seed2soil":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            seed2soil.append(line)
        elif line == "soil-to-fertilizer map:":
            import_mode = "soil2fertilizer"
        elif import_mode == "soil2fertilizer":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            soil2fertilizer.append(line)
        elif line == "fertilizer-to-water map:":
            import_mode = "fertilizer2water"
        elif import_mode == "fertilizer2water":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            fertilizer2water.append(line)
        elif line == "water-to-light map:":
            import_mode = "water2light"
        elif import_mode == "water2light":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            water2light.append(line)
        elif line == "light-to-temperature map:":
            import_mode = "light2temp"
        elif import_mode == "light2temp":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            light2temp.append(line)
        elif line == "temperature-to-humidity map:":
            import_mode = "temp2humidity"
        elif import_mode == "temp2humidity":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            temp2humidity.append(line)
        elif line == "humidity-to-location map:":
            import_mode = "humidity2location"
        elif import_mode == "humidity2location":
            line = line.split()
            for i_b,num in enumerate(line):
                line[i_b] = int(line[i_b])
            humidity2location.append(line)
        

seeds = np.array(seeds,dtype=object)
seeds = seeds[:,np.newaxis]
seeds = np.pad(seeds, ((0,0),(0,7)),mode="constant",constant_values=0)
#This has made a storage array with a least of seeds in column 0.
#The additional items related to each seed are shown in subsequent columns:
#Seed Soil Fertilizer Water Light Temperature Humidity Location
#print("The list of seeds is:")
#print(seeds)
#print("The dictionary to convert seeds to soil types is: ")
#print(seed2soil)
#print("The dictionary to convert soil to fertilizer is: ")
#print(soil2fertilizer)
#print("The dictionary to convert fertilizer to water is: ")
#print(fertilizer2water)
#print("The dictionary to convert water to light is: ")
#print(water2light)
#print("The dictionary to convert light to temperature is: ")
#print(light2temp)
#print("The dictionary to convert temperature to humidity is: ")
#print(temp2humidity)
#print("The dictionary to convert humidity to location is: ")
#print(humidity2location)

#a = seed2soil.get(9000)
#print(a)
#if a == None:
#    print("yay")


###Initial Conditions

###Main Code
for i_c,seed in enumerate(seeds):#Iterates over each line and fills in all info
    
    #Seed to Soil
    seed[1] = convert_A_to_B(seed[0],seed2soil)
    #Soil to Fertilizer
    seed[2] = convert_A_to_B(seed[1],soil2fertilizer)
    #Fertilizer to Water
    seed[3] = convert_A_to_B(seed[2],fertilizer2water)
    #Water to Light
    seed[4] = convert_A_to_B(seed[3],water2light)
    #Light to Temperature
    seed[5] = convert_A_to_B(seed[4],light2temp)
    #Temperature to Humidity
    seed[6] = convert_A_to_B(seed[5],temp2humidity)
    #Humidity to Location
    seed[7] = convert_A_to_B(seed[6],humidity2location)
    
    #print(seed)

#print(seeds)
result = min(seeds[:,7])

###Result
print(result)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")