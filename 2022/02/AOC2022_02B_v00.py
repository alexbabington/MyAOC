#Advent of code 2022
#Day 02 Part 2
#Rock Paper Scissors

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

#Functions

#Define Rocks, Papers, and Scissors
translate_to_RPS = {}
translate_to_RPS["A"] = "R"
translate_to_RPS["B"] = "P"
translate_to_RPS["C"] = "S"

translate_to_score = {}
translate_to_score["R"] = 1
translate_to_score["P"] = 2
translate_to_score["S"] = 3

find_winner = {}
find_winner["R"] = "P"
find_winner["P"] = "S"
find_winner["S"] = "R"

find_loser = {}
find_loser["R"] = "S"
find_loser["P"] = "R"
find_loser["S"] = "P"

#Import and sort File
rival = []
elf = []

with open("input_02.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        line = line.split(" ")
        
        rival.append(translate_to_RPS[line[0]])
        elf.append(line[1])

###Main Code
total_score = 0

for i, rival_play in enumerate(rival):
    elf_result = elf[i]
    
    if elf_result == "Y":
        #Draw
        elf_play = rival_play
        result = 3
    elif elf_result == "Z":
        #Win
        elf_play = find_winner[rival_play]
        result = 6
    elif elf_result == "X":
        #Lose
        elf_play = find_loser[rival_play]
        result = 0
    
    value = translate_to_score[elf_play]
    
    score = result + value
    total_score += score

#Result
print(total_score)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")