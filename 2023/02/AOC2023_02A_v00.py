#Advent of code 2023
#Day 2 Part 1
#Cube Conundrum

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
list_of_games = []

with open("input_02.txt") as input_dataf:
    for ia,line in enumerate(input_dataf):
        #Import operations
        line = line.strip("\n")#Remove EOL symbol
        
        line = line.split(": ")#Split by game id and info seperator
        line = line[1]#continue with data only
        
        line = line.split("; ")#Splits each game into subsets
        
        game = []#Blank game to write into
        for ib,set in enumerate(line):
            #Runs through each subset and records cubes shown
            set = set.split(", ")#Splits subset into list of balls
            subset = [0,0,0]#Starts blank subset to write into of format red,green,blue
            for ic,ball in enumerate(set):
                #Iterates through each set and records the balls
                ball = ball.split(" ")
                quantity = int(ball[0])
                colour = ball[1]
                
                if colour == "red":
                    subset[0] = quantity
                elif colour == "green":
                    subset[1] = quantity
                elif colour == "blue":
                    subset[2] = quantity
                else:
                    print("ERROR: The colour is invalid")
                    print("The colour is ",colour)
                    print("The quantity is ",quantity)
                    print("The line being evaluated form the input file is ",line)
                    print("The subset being evaluated is ",set)
                    print("The ball being evaluates is ",ball)
                    pdb.set_trace()
            
            game.append(subset)#Writes subset to game
        
        list_of_games.append(game)#Writes game to list of games

list_of_games = np.array(list_of_games,dtype=object)

###Initial Conditions
balls_in_the_bag = [12,13,14]
sum_of_game_ids = 0

###Main Code
for i_d,game in enumerate(list_of_games):#Iterates through each game and checks if valid
    valid = True#Booleen changed to false if game fails any conditions
    
    for i_e,subset in enumerate(game):#Iterates through each subset and checks validity of balls
        for i_f,quantity in enumerate(subset):#Gets the quantity for every ball
            if quantity > balls_in_the_bag[i_f]:#Checks if more balls were pulled than those available and invalidates if true
                valid = False
    
    if valid == True:#adds game id to list of valid ids if games is still valid
        sum_of_game_ids = sum_of_game_ids + i_d + 1




###Result
print(sum_of_game_ids)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")