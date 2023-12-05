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
#def function(inputs):
#    #Function
#
#    return outputs

###Import and sort File
seeds = []
seed2soil = {}
soil2fertilizer = {}
fertilizer2water = {}
water2light = {}
light2temp = {}
temp2humidity = {}
humidity2location = {}

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
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                seed2soil[source] = destination
                source += 1
                destination += 1
                i_b -= 1
        elif line == "soil-to-fertilizer map:":
            import_mode = "soil2fertilizer"
        elif import_mode == "soil2fertilizer":
            line = line.split()
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                soil2fertilizer[source] = destination
                source += 1
                destination += 1
                i_b -= 1
        elif line == "fertilizer-to-water map:":
            import_mode = "fertilizer2water"
        elif import_mode == "fertilizer2water":
            line = line.split()
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                fertilizer2water[source] = destination
                source += 1
                destination += 1
                i_b -= 1
        elif line == "water-to-light map:":
            import_mode = "water2light"
        elif import_mode == "water2light":
            line = line.split()
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                water2light[source] = destination
                source += 1
                destination += 1
                i_b -= 1
        elif line == "light-to-temperature map:":
            import_mode = "light2temp"
        elif import_mode == "light2temp":
            line = line.split()
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                light2temp[source] = destination
                source += 1
                destination += 1
                i_b -= 1
        elif line == "temperature-to-humidity map:":
            import_mode = "temp2humidity"
        elif import_mode == "temp2humidity":
            line = line.split()
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                temp2humidity[source] = destination
                source += 1
                destination += 1
                i_b -= 1
        elif line == "humidity-to-location map:":
            import_mode = "humidity2location"
        elif import_mode == "humidity2location":
            line = line.split()
            source = int(line[1])
            destination = int(line[0])
            i_b = int(line[2])
            while i_b > 0:
                humidity2location[source] = destination
                source += 1
                destination += 1
                i_b -= 1

seeds = np.array(seeds,dtype=object)
seeds = seeds[:,np.newaxis]
seeds = np.pad(seeds, ((0,0),(0,7)),mode="constant",constant_values=0)
#This has made a storage array with a least of seeds in column 0.
#The additional items related to each seed are shown in subsequent columns:
#Seed Soil Fertilizer Water Light Temperature Humidity Location
print("The list of seeds is:")
print(seeds)
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
    
    #Seed2Soil
    temp = seed2soil.get(seed[0])
    if temp == None:
        seed[1] = seed[0]
    else:
        seed[1] = temp
    
    print(seeds)
    
    #Soil2Fertilizer
    temp = soil2fertilizer.get(seed[1])
    if temp == None:
        seed[2] = seed[1]
    else:
        seed[2] = temp
    
    print(seeds)
    
    #Fertilizer2Water
    temp = fertilizer2water.get(seed[2])
    if temp == None:
        seed[3] = seed[2]
    else:
        seed[3] = temp
    
    print(seeds)
    
    #Water to light
    temp = water2light.get(seed[3])
    if temp == None:
        seed[4] = seed[3]
    else:
        seed[4] = temp
    
    print(seeds)
    
    #Light to temp
    temp = light2temp.get(seed[4])
    if temp == None:
        seed[5] = seed[4]
    else:
        seed[5] = temp
    
    print(seeds)
    
    #Temp to humidity
    temp = temp2humidity.get(seed[5])
    if temp == None:
        seed[6] = seed[5]
    else:
        seed[6] = temp
    
    print(seeds)
    
    #Humidity to Location
    temp = humidity2location.get(seed[6])
    if temp == None:
        seed[7] = seed[6]
    else:
        seed[7] = temp
    
    print(seeds)

#print(seeds)
result = min(seeds[:,7])

###Result
print(result)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")