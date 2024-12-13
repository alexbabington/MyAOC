#Advent of code 2024
#Day 9 Part 1
#Disk Fragmenter

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
with open("input_09_test.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = list(map(int,line))
        
        
        
        input.append(line)

diskmaparray = np.array(input[0],dtype=object)

#print(diskmaparray)

###Initial Conditions
#files = []
#freespaces = []
diskmap = []

###Main Code
#sort through and store data into files or freespaces
#format is: [id, size of block]
for i_a,size in enumerate(diskmaparray):
    if i_a % 2 == 0:
        entry = [int(i_a/2),size]
        #files.append(entry)
        diskmap.append(entry)
    else:
        #freespaces.append(size)
        diskmap.append(["null",size])

#print("files are")
#print(files)
#print("freespace is")
#print(freespaces)
#print("diskmap is")
#print(diskmap)

new_diskmap = []

#Amphipod Iterate through diskamp and pull parts from end
for i_b,entry in enumerate(diskmap):
    #print("Entry is ",entry)
    #print("diskmap is ",diskmap)
    #print("new diskmap is ",new_diskmap)
    if entry[0] == "null":
        if i_b < (len(diskmap) - 2):
            #Only move if dealing with free space
            blocks_to_fill = entry[1]
            new_entrys = []
            
            #pull enough files from end to fill
            while blocks_to_fill > 0:
                end_entry = diskmap[-1]
                del diskmap[-1]
                if end_entry[0] == "null":
                    continue
                else:
                    blocks_to_fill -= end_entry[1]
                    new_entrys.append(end_entry)
                    #pdb.set_trace()
            
            if blocks_to_fill == 0:
                for new_entry in new_entrys:
                    #print("New entry is ",new_entry)
                    new_diskmap.append(new_entry)
            else:
                del new_entrys[-1]
                if len(new_entrys) >= 0:
                    entered = 0
                    for new_entry in new_entrys:
                        entered += new_entry[1]
                        #print("New entry is ",new_entry)
                        new_diskmap.append(new_entry)
                entry_to_steal = [end_entry[0],entry[1]-entered]
                #print("new stolen entry is ",entry_to_steal)
                new_diskmap.append(entry_to_steal)
                entry_to_return = [end_entry[0],abs(blocks_to_fill)]
                diskmap.append(entry_to_return)
        
    else:
        #File copy directly
        #print("Existing entry copied ",entry)
        new_diskmap.append(entry)
    
    
    
    

#print("diskmap after amphipod is ")
#print(new_diskmap)

#Create Checksum
checksum = 0
id = 0
for entry in new_diskmap:
    entrystr = entry[1] * str(entry[0])
    print(entrystr)
    for char in entrystr:
        char = int(char)
        sum = char * id
        checksum += sum
        id += 1

###Result
print("The checksum is ",checksum)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")