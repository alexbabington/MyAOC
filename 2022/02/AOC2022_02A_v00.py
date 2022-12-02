#Advent of code 2022
#Day 02 Part 1
#Rock Paper Scissors

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

#Functions
def janken_pon(rival_play,your_play):
    #Takes a play and returns if you won
    #rival_play - rivals play can be "R","P","S"
    #your_play - your play can be "R","P","S"
    #result - 0 = lost, 3 = draw, 6 is won
    #Rules:
    #"R" beats "S"
    #"S" beats "P"
    #"P" beats "R"
    
    if rival_play == your_play:
        #Game is a draw
        result = 3
    elif rival_play != "P" and your_play != "P":
        #Game with Rock and Scissor only. Rock wins
        if your_play == "R":
            #Win
            result = 6
        else:
            #Lose
            result = 0
    elif rival_play != "R" and your_play != "R":
        #Game with Paper and Scissor only. Scissor wins
        if your_play == "S":
            #Win
            result = 6
        else:
            #Lose
            result = 0
    elif rival_play != "S" and your_play != "S":
        #Game with Rock and Paper only. Paper wins
        if your_play == "P":
            #Win
            result = 6
        else:
            #Lose
            result = 0
    
    return result

#Define Rocks, Papers, and Scissors
translate_to_RPS = {}
translate_to_RPS["A"] = "R"
translate_to_RPS["B"] = "P"
translate_to_RPS["C"] = "S"
translate_to_RPS["X"] = "R"
translate_to_RPS["Y"] = "P"
translate_to_RPS["Z"] = "S"

translate_to_score = {}
translate_to_score["R"] = 1
translate_to_score["P"] = 2
translate_to_score["S"] = 3

#Import and sort File
rival = []
elf = []

with open("input_02.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        line = line.split(" ")
        
        rival.append(translate_to_RPS[line[0]])
        elf.append(translate_to_RPS[line[1]])

###Main Code
total_score = 0

for i, rival_play in enumerate(rival):
    elf_play = elf[i]
    
    result = janken_pon(rival_play,elf_play)
    
    value = translate_to_score[elf_play]
    
    score = result + value
    total_score += score

#Result
print(total_score)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")