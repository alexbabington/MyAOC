#Advent of code 2023
#Day 4 Part 1
#Scratchcards

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def match_numbers(guesses,answers):
    #Takes a list of guesses and returns and which appear in the answers list
    matches = []
    for i_b,guess in enumerate(guesses):
        if guess in answers:
            matches.append(guess)
    
    return matches

###Import and sort File
input = []

with open("input_04.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = line.split(": ")#Split off card number
        line = line[1]
        line = line.split(" | ")
        for i_a,side in enumerate(line):
            line[i_a] = line[i_a].split()
            line[i_a] = [eval(i) for i in line[i_a]]
        
        
        input.append(line)

cards = np.array(input,dtype=object)

#print(cards)

###Initial Conditions
overall_points = 0

###Main Code
for i_c,card in enumerate(cards):#Evaluates each card individually to determine score
    winning_numbers = match_numbers(card[1],card[0])
    no_of_wins = len(winning_numbers)
    if no_of_wins > 0:
        points = 2**(no_of_wins-1)
    else:
        points = 0
    #print("No of wins was: ",no_of_wins,". No of points scored was: ",points)
    overall_points += points



###Result
print(overall_points)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")