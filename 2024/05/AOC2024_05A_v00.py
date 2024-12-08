#Advent of code 2024
#Day 5 Part 1
#Print Queue

import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import pdb #pdb.set_trace()
import time
import copy

start_time = time.time()

###Constants

###Functions
def eval_page_compliance(page,rules):
    #Function to evaluate if a page is compliant to a list of rules
    
    compliance_list = []
    
    #print("Evaluating if the following pages is valid")
    #print("Page: ",page)
    
    
    for i_b,rule in enumerate(rules):
        #Check rule is relevant
        #print("Evaluating if following rule is relevant")
        #print("Rule: ",rule)
        if (rule[0] in page) and (rule[1] in page):
            #print("Rule is relevant")
            before_index = page.index(rule[0])
            after_index = page.index(rule[1])
            
            if before_index < after_index:
                #print("Page compliant rule")
                compliance_list.append(True)
            else:
                #print("not compliant to rule")
                compliance_list.append(False)
                
                #Swap Numbers to make compliant to rule
                print(page)
                
                page[before_index] = rule[1]
                page[after_index] = rule[0]
                
                print(page)
                pdb.set_trace()
    
    if all(compliance_list):
        compliant_bool = True
        #print("Page is compliant to all rules")
    else:
        compliant_bool = False
        #print("Page not compliant")
    
    return compliant_bool,page

###Import and sort File
rules = []
pages = []
section = "rules"

with open("input_05_test.txt") as input_dataf:
    for i,line in enumerate(input_dataf):
        #Import operations
        
        line = line.strip("\n")#Remove EOL symbol
        
        
        if line == "":
            section = "pages"
        else:
            if section == "rules":
                line = line.split("|")
                line = list(map(int,line))
                rules.append(line)
            
            if section == "pages":
                line = line.split(",")
                line = list(map(int,line))
                pages.append(line)

rules = np.array(rules,dtype=object)

#print(rules)
#print(pages)

###Initial Conditions
no_compliant = 0
sum_of_compliant_middles = 0
###Main Code
for i_a,page in enumerate(pages):
    compliant_bool = False
    i_b = 0
    print("Page is ")
    
    while compliant_bool == False:
        #Eval if page is compliant
        [compliant_bool,page] = eval_page_compliance(page,rules):
        print(compliant_bool)
        if compliant_bool == True:
            print("Page is compliant")
            no_compliant += 1
            #Find middle number
            middle_index = int((len(page) - 1)/2)
            sum_of_compliant_middles += page[middle_index]


###Result
print("The number of compliant lines is ",no_compliant)
print("The sum of the compliant middles is ",sum_of_compliant_middles)

timetaken = time.time() - start_time
print("Completed in ", timetaken, " seconds")