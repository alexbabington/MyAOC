#Advent of code 2023
#Day 7 Part 1
#Camel Cards

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy
from collections import Counter

start_time = time.time()

###Constants
type_dict = {}
type_dict["5kind"] = 7
type_dict["4kind"] = 6
type_dict["full_house"] = 5
type_dict["3kind"] = 4
type_dict["2pair"] = 3
type_dict["1pair"] = 2
type_dict["high_card"] = 1

card_rank_dict = {}
card_rank_dict["A"] = 13
card_rank_dict["K"] = 12
card_rank_dict["Q"] = 11
card_rank_dict["J"] = 10
card_rank_dict["T"] = 9
card_rank_dict["9"] = 8
card_rank_dict["8"] = 7
card_rank_dict["7"] = 6
card_rank_dict["6"] = 5
card_rank_dict["5"] = 4
card_rank_dict["4"] = 3
card_rank_dict["3"] = 2
card_rank_dict["2"] = 1

###Functions
def determine_hand_type(hand):
    #Takes and hand of cards and determines the type of the hand. Gives this as a number
    #5 of a kind        = 7
    #4 of a kind        = 6
    #full house         = 5
    #3 of a kind        = 4
    #2 pair             = 3
    #1 pair             = 2
    #High card          = 1
    
    counts = Counter(hand)
    counts_list = counts.most_common()
    
    if counts_list[0][1] == 5:
        #Five of a kind
        type = 7
    elif counts_list[0][1] == 4:
        #Four of a kind
        type = 6
    elif counts_list[0][1] == 3 and len(counts) == 2:
        #Full House
        type = 5
    elif counts_list[0][1] == 3:
        #Three of a kind
        type = 4
    elif counts_list[0][1] == 2 and len(counts) == 3:
        #2 Pair
        type = 3
    elif counts_list[0][1] == 2:
        #1 Pair
        type = 2
    elif counts_list[0][1] == 1 and len(counts) == 5:
        #High Cards
        type = 1
    else:
        print("ERROR: determine_hand_type function has failed to find a hand type")
        print("The cards in the hand were: ",hand)
        pdb.set_trace()
    
    return type

###Import and sort File
#input = [["hand","bid","type","rank1","rank2","rank3","rank4","rank5"]]
input = []

with open("input_07.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        line = line.split()
        line[1] = int(line[1])
        
        line = line + [0,0,0,0,0,0]
        
        line = tuple(line)
        
        input.append(line)

#print(input)

dt = np.dtype([("hand",np.unicode_,5),("bid",int),("type",int),("rank1",int),("rank2",int),("rank3",int),("rank4",int),("rank5",int)])
plays = np.array(input,dtype=dt)

#print(plays)
#print(" ")
#Plays are now shown in format
#Hand, bid, type, 1st card rank, 2nd card rank, 3rd card rank, 4th card rank, 5th card rank


###Initial Conditions

###Main Code
for i_a,play in enumerate(plays):
    hand = play[0]
    bin = play[1]
    type = determine_hand_type(hand)
    play[2] = type
    play[3] = card_rank_dict[hand[0]]#Determines ranks of 1st card
    play[4] = card_rank_dict[hand[1]]#Determines ranks of 2nd card
    play[5] = card_rank_dict[hand[2]]#Determines ranks of 3rd card
    play[6] = card_rank_dict[hand[3]]#Determines ranks of 4th card
    play[7] = card_rank_dict[hand[4]]#Determines ranks of 5th card
    
    
    
    #print("This hand is: ",hand)
    #print("The type is: ",type)
    #print("This play is: ",play)

#Sort plays from strongest to weakest
#print(plays)
#print(" ")
plays_sorted = np.sort(plays, order=["type","rank1","rank2","rank3","rank4","rank5"])


#print(plays_sorted)


#Find Winnings
winnings = 0
for i_b,play in enumerate(plays_sorted):
    winnings += play[1] * (i_b+1)

###Result
print(winnings)


timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")