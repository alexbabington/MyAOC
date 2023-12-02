#Advent of code 2023
#Day 2 Part 2
#Cube Conundrum

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy
import math

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
sum_of_game_min_powers = 0

###Main Code
for i_d,game in enumerate(list_of_games):#Iterates through each game and checks if valid
    min_balls_needed = [0,0,0]
    
    for i_e,subset in enumerate(game):#Iterates through each subset and checks validity of balls
        for i_f,quantity in enumerate(subset):#Gets the quantity for every ball
            if quantity > min_balls_needed[i_f]:#Checks if more balls are needed to achieve the draw and updates game min balls if so
                min_balls_needed[i_f] = quantity
    
    #print(min_balls_needed)
    
    min_power = math.prod(min_balls_needed)
    
    #print(min_power)
    
    sum_of_game_min_powers += min_power




###Result
print(sum_of_game_min_powers)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")