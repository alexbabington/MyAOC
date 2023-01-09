#Advent of code 2022
#Day 11 Part 2
#Monkey in the Middle

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy
import math
import operator

start_time = time.time()

###Functions
def inspect_item(item,monkey,test_value_product):
    #Takes an item stored by a monkey, inspects it according to the rules of that monkey, and then returns which monkey to throw it to
    #Inputs:
    #   -   item - the item worry level to be inspected
    #   -   monkey - the monkey which will be inspecting the item
    #Outputs:
    #   -   monkey_no_to_throw_to - the number of the monkey to throw the item too
    #   -   item - the new item worry level
    
    #Retrieve information about the monkey doing the inspection
    operation_type = monkey[1]
    operation_value = monkey[2]
    test_type = monkey[3]
    test_value = monkey[4]
    monkey_if_true = monkey[5]
    monkey_if_false = monkey[6]
    
    item_mod = item%test_value_product
    op_mod = operation_value%test_value
    
    #print(test_value_product)
    #print(item)
    #print(item_mod)
    #print(operation_value)
    #print(op_mod)
    #pdb.set_trace()
    
    #Perform Operation to increase worry level
    if operation_type == "multiply":#Multiply item by the operation value
        item *= operation_value
        test_mod = (item_mod * op_mod)%test_value
    elif operation_type == "power":#Times item value by itself a set number of times
        item = item**operation_value
        test_mod = (item_mod ** 2)%test_value
    elif operation_type == "add":#Add the operation value to the item value
        item += operation_value
        test_mod = (item_mod + op_mod)%test_value
    else:#Catches operations which have not been programmed
        print("ERROR: the operation type was not regongnised")
        pdb.set_trace()
    
    #Reduce worry level by floor(worry/3) as the monkey didn't damage the item
    #COMMENTED OUT FOR PART 2
    #item = math.floor(item/3)
    
    #Test where monkey should throw the item to
    if test_type == "divisible":#Performs a divisible type test
        #remainder = item/test_value - math.floor(item/test_value)#Finds the value after the decimel point post division
        #remainder = item%test_value#Finds the value after the decimel point post division
        #if remainder == 0:
        if test_mod == 0:
            test_result = True
        else:
            test_result = False
    else:#Catches tests which have not been programmed
        print("ERROR: the test type was not regongnised")
        pdb.set_trace()
    
    if test_result == True:
        monkey_no_to_throw_to = monkey_if_true
    elif test_result == False:
        monkey_no_to_throw_to = monkey_if_false
    else:#Cathces invalid test results
        print("ERROR: the test result was invalid")
        pdb.set_trace()
    
    #Check sum
    new_item_mod = item%test_value_product
    #if test_mod != new_item_mod:
    #    print("test_mod and new item mod do not agree")
    #    pdb.set_trace()
    
    
    return monkey_no_to_throw_to, new_item_mod

###Import and sort File
monkeys = []#A list of all the monkeys
monkey = []#A simple list format storing information about each monkey in the form [list_of_items,operation_type,operation_value,test_type,test_value,monkey_if_true,monkey_if_false]

with open("input_11.txt") as input_dataf:
    for line in input_dataf:
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        line = line.split()#Split and remove whitespace
        
        if line == []:#Expected lines do nothing
            shit = 1
        elif line[0] == "Monkey":#Expected lines do nothing
            shit = 1
        elif line[0] == "Starting":#Format and store staring values for this monkey
            line = line[2:]#Strip to just values
            for i,item in enumerate(line):
                line[i] = line[i].strip(",")
                line[i] = int(line[i])
            monkey.append(line)#Store into list for monkey
        elif line[0] == "Operation:":#Format and store the operation type and operation value
            if line[4] == "*" and line[5] == "old":
                operation_type = "power"
                operation_value = 2
            elif line[4] == "*":
                operation_type = "multiply"
                operation_value = int(line[5])
            elif line[4] == "+":
                operation_type = "add"
                operation_value = int(line[5])
            else:#Catch any unrecognised operations
                print("ERROR: Operation not recognised")
                pdb.set_trace()
            monkey.append(operation_type)
            monkey.append(operation_value)
        elif line[0] == "Test:":#Format and store the test type and test value
            if line[1] == "divisible":
                test_type = line[1]
                test_value = int(line[3])
            else:#Catch any unrecognised tests
                print("ERROR: Test not recognised")
                pdb.set_trace()
            monkey.append(test_type)
            monkey.append(test_value)
        elif line[0] == "If" and line[1] == "true:":#Format and store the monkey to throw to if true
            monkey_if_true = int(line[5])
            monkey.append(monkey_if_true)
        elif line[0] == "If" and line[1] == "false:":#Format and store the monkey to throw to if false
            monkey_if_false = int(line[5])
            monkey.append(monkey_if_false)
            
            #This monkey is complete, clear the current monkey
            #print("Monkey read and stored as ",monkey)
            monkeys.append(monkey)
            monkey = []
        else:
            print(line)
            print("Unexpected line in input file")
            pdb.set_trace()

###Initial Conditions
no_rounds = 10000
#Setup blank list for number of monkey inspections
no_of_inspections = [0] * len(monkeys)
no_of_inspections_old = [0] * len(monkeys)
#list of round numbers to print
#print_rounds = [1,20,100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
print_rounds = [10000]

###Main Code
#Calculate product of test values
test_value_product = 1
for monkey in monkeys:
    test_value_product *= monkey[4]

round = 0
#Perform all the rounds
while round < no_rounds:
    #Iterate through all the monkeys
    for i,monkey in enumerate(monkeys):
        items_held = monkey[0]
        #For each item held by the monkey inspect and throw it
        for k,item in enumerate(items_held):
            [monkey_no_to_throw_to, item] = inspect_item(item,monkey,test_value_product)#Performs the inspection by the monkey
            no_of_inspections[i] += 1#Logs the inspection was performed
            monkeys[monkey_no_to_throw_to][0].append(item)#throws the item to the other monkey
        #Remove all the items from the monkey doing the throwing
        monkeys[i][0] = []
    
    #Print resut of round
    ##print("Round number is ",round+1)
    if round+1 in print_rounds:
        ##print("")
        print("After round ",round+1," the results are")
        #for monkey in monkeys:
        #    print("This monkey is ",monkey)
        #print("")
        no_of_inspections_sorted = sorted(no_of_inspections,reverse=True)
        result = no_of_inspections_sorted[0] * no_of_inspections_sorted[1]
        ##print("The number of inspections performed by each monkey is")
        print(no_of_inspections)
        ##print("")
        ##print("The product of the number of inspections performed by the 2 most active monkeys is:")
        ##print(result)
        ##print("")
        #diff = []
        #for a,thing in enumerate(no_of_inspections):
        #    diff.append(no_of_inspections[a]-no_of_inspections_old[a])
        #print(diff)
        #no_of_inspections_old = copy.deepcopy(no_of_inspections)
    
    round += 1

###Result
#print("The number of inspections performed by each monkey is")
#print(no_of_inspections)
#print("")
print("The product of the number of inspections performed by the 2 most active monkeys is:")
print(result)


timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")