"""  
Program name: EECS210_Assignment 5
Brief Description: The main point of this project is to prove if relations and sets are either injective, surjective, bijective, and implememting algorithms to find the gcd of a function
Inputs: There are no inputs 
Output: 4 different outputs
All collaborators: Chat-GPT, Yaeesh M., Zonaid P, Arnav J. ,;
Author's full name: Humza Ahmed Qureshi
Creation date: 10-22-2023

"""



def is_func(function):# function defining if a function is a function
    hash_map = {} # create a hssh map to add keys values to the dicitionary
    for (ele1,ele2) in function:# for the ele1, and ele2 repsecitallty for the tuple
        key, value  = ele1, ele2# map key and value to ele1 and ele2
        if key in hash_map:# if the key is already in the hashmap
            return False# then they will return false
        else:# if this is not the case
            hash_map[key] = value# then update the dictionary
    return True# if this never happens to where a key is already in the dictionary, then the function will return true 
"""
Author combination: Chat-GPT
"""
def injective(function):# function definition proving that the function is injective or not
    hash_map = {}# create a hssh map to add keys values to the dicitionary
    for (ele1,ele2) in function:# for the ele1, and ele2 repsecitallty for the tuple
        key = ele2# map key to ele2
        if key in hash_map:# if the key is already in the hashmap
            return False #then they will return false
        hash_map[key] = 1 + hash_map.get(key, 0)# if this is not the case, update the hash map
    return True # if the key is never in the hash, then return true

def surjective(function, cdomain):# function definition provinf that the function is surjective or not
    hash = {}# create a dictionary
    for ele in cdomain:# for all the elements in the cdomain
        hash[ele] = 1 + hash.get(ele, 0)# build the dictionary

    for coor in function:# for cooridates in the function
        domain, codomain = coor# assignment domain and codomain to repsective coordinate
        if codomain not in hash:# if the second element is not in the hash
            return False# then you will return false
    return True # other wise return true

def bijective(function, codomain):# defining a function to prove if a function is bijective or not
    return surjective(function, codomain) and injective(function)# if the function is surjective and injective, then it will return true or false respectivily

def inverse(function):# find the inverse of the function
    new_function = {}# define a hash map
    new_list = []# define a list
    for ele in function:# for the elements in the function
        tupeele1, tupeele2 = ele # set tuple element 1 and 2 to the respective elements of functions
        k = tupeele2# set key to tup 2
        v = tupeele1# set value to tup 1
        new_function[k] = v# build the hash map
    for key, value in new_function.items():# iterate through the dictionary
        tup = key,value# create a tup of the functions
        new_list.append(tup)# append the tup to the new_list
    return new_list # return the new list



def question1():# a function putting everything together
    print("--" * 40)# formatting
    """
    Creating the sample points of the expected output given in the assignment
    """
    sample_points = [
        ({"a","b","c","d"}, {"v","w","x","y","z"},{("a","z"),("b","y"),("c","x"),("d","w")}),
        ({"a","b","c","d"}, {"x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","z")}),
        ({"a","b","c","d"}, {"w","x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","w")}),
        ({"a","b","c","d"}, {1,2,3,4,5}, {("a",4),("b",5),("c",1),("d",3)}),
        ({"a","b","c"}, {1,2,3,4}, {("a",3),("b",4),("c",1)}),
        ({"a","b","c","d"}, {1,2,3}, {("a",2),("b",1),("c",3),("d",2)}),
        ({"a","b","c","d"}, {1,2,3,4}, {("a",4),("b",1),("c",3),("d",2)}),
        ({"a","b","c","d"}, {1,2,3,4}, {("a",2),("b",1),("c",2),("d",3)}),
        ({"a","b","c"}, {1,2,3,4}, {("a",2),("b",1),("a",4),("c",3)})
    ]   
    
    for aset,bset, fset in sample_points:# iterate through the three elements in the list
        print(f'A = {aset}, B = {bset}, f = {fset}')# print these elements for formatting reasons

        if is_func(fset):# prove that the function is a function
            print("This is a function")# if the function method agrees that the function is a function, return true or false 
        else:# if it is false, then the output .....
            print("This is not a function, so it cannot be Injective, surjectice, or bijective")# will be this output message
            continue# stop the loop so it dosent check anything else

        if injective(fset):# check if the function is injective or not
            print(f'This function is injective')# if the function agrees that the function is infact injective, then the message will print
        else:# if the function is not injective, then the program will output this messahe
            print(f'This function is not injective')# print this message 
        if surjective(fset, bset):# check to see if the surjective function is the following
            print(f'This function is surjective')# if the surjective function agrees that the function is true
        else:# then output the following
            print(f'This function is not surjective')# if it is false, then outpuyt the rest
        if bijective(fset, bset):# if both surjective and injective, then true, if not then false
            print(f'This function is bijective')# print out this
            print(f'The inverse of the function includes: {inverse(fset)}')# and then check what the inverse of the function will be
        else:# if this is not true
            print(f'This function is not bijective')# simply output this functiuon messaged

        print("--" * 40)# formatting
        
def euclidean_algorithm(tup):# definition of the eucldiean algorithm
    numer = max(tup)# check which numer is the max
    denom = min(tup)# check which integer in the tuple is the min value

    while numer:# while the numer exists ( will alwaty exist)
        print(f'{numer}/{denom} = {numer//denom} R {numer % denom}')# print out the following message
        numer, denom = denom, numer % denom# then switch the integers; numer points to denom and denom points to numer mod denom
        if numer % denom == 0:# if the mod eventually equals 0
            print(f'{numer}/{denom} = {numer//denom} R {numer % denom}')# out put the final message
            break# and then break the loop
    return denom# then return the denom of the function
def euclidean_algorithm_final(tup):# function to not output the print statement of the above function
    numer = max(tup)# max integer goes to the top
    denom = min(tup)# min integer goes to the bottom

    while numer:# while the numer exists (this will always exist)
        numer, denom = denom, numer % denom# switch the values around
        if numer % denom == 0:# if the num mod denom is 0
            break# break the loop completlty
    return denom# return the denom of the function
def return_gcd(tup):# function to just return the gcd of the function
    result = euclidean_algorithm_final(tup)# set the gcd to the result of the function
    return result# will return result


def question2():# define method for question 2
    print("--" * 40)
    sample = [(414,662), (6,14), (24,36), (12,42), (252, 198)]# sample points
    for tup in sample:
        print("------------------------                      ")# formatting
        print(f'GCD({tup})')# formatting
        print("------------------------                      ")
        euclidean_algorithm(tup)# run through the euclidean algorithn to find the steps of the algorithm
        print(f'GCD({tup}) = {return_gcd(tup)}')# at the end, print the gcd of the tuple
        print("------------------------                      ") # formatting

        

def extended_gcd_steps(tup):# extended version of gcd steps
    numer = max(tup)# max integer
    denom = min(tup)# min integer
    temp_integer_d = numer // denom# to integer division for formatting reasons

    while numer:# while numer exists, ( will always exist) continue the loop
        print(f'{numer} = {denom} * {temp_integer_d} + {numer%denom}')# print statment (formatting)
        numer, denom = denom, numer % denom# switch the values of the numer and denom
        temp_integer_d = numer // denom# set the integer of the function
        if numer % denom == 0:# if the num mod denom is 0, then it will be 0
            print(f'{numer} = {denom} * {temp_integer_d} + {numer%denom}')# print the final message
            break# the loop
    return # then return the gcd steps
steps = []# create a global variable that all can look at
def gcd_steps(tup):# copy and paste function so that it does not have print messsage, but instead for internal use
    numer = max(tup)# max integer
    denom = min(tup)# min integer
    temp_integer_d = numer // denom# to integer division for formatting reasons

    while numer:# while numer exists, ( will always exist) continue the loop
        numer, denom = denom, numer % denom# switch the values of the numer and denom
        temp_integer_d = numer // denom# set the integer of the function
        steps.append([numer, denom, temp_integer_d])# append the steps to the list
        if numer % denom == 0:# if the num mod denom is 0
            break# break the loop
    return steps# access the list by returning 
"""
Author combination: Arnav J. and Zonaid P. 
"""
def egcd_backwards(tup): # define a function that returns 
    a = max(tup)
    #set x as the max of a and b
    b = min(tup)
    #set y as the min of a and b
    backwards_list = []# create an empty list
    while b!=0:# while the remainder of the list is B
        r = a%b # the remainder of the r is the mod between a and b
        print(f'{a} = {b} * {a//b} + {r}') # print statement
        backwards_list.append([a,b,a//b,r])# will append max, min, integer divison, remainder
        a=b# set a equal to b
        b=r# set b equal to remainder
    gcd = return_gcd(tup)# the gcd of the functiuon is passing through the function
    backwards_list.pop()# pop the list of the backwards list as this part of the list is unnessecary
    backwards_list = backwards_list[::-1]# now reverse the list
    last = backwards_list[0]# the last part if the list is the first part of the equation now
    s =1 # set the coeffient of s to 1
    result, lastx, lasty, lastz = last[3], last[0], last[1], last[2]# set all of these functions equal to eachother
    checker = None# create a checker variable 
    for a,b,integer,r in backwards_list[1:]: # iterate through the backwards list 
        print(f"{result} = {s} * {lastx} - {lastz}*{lasty}")# print the printing message
        checker =1 if lasty == r else 0 if lastx == r else -1# if the checker equal 1, if lasty equals the remainder; 
        if checker ==1:# if the checker equals 1
            print(f"{result} = {s} * {lastx}-{lastz} * ({a} - {integer}*{b})")# print this
            s = lastz*integer +s# updates the s variable
            lasty =a # update the lasty variable
        elif checker == 0:# if the checker equals 0
            print(f"{result} = {s} *({a} - {integer}*{b}) - {lastz}*{lasty}")# print this format
            lastz= s*integer+lastz# update the lastz
            lastx = a # update the lastz
    print(f"{result} = {s} *{lastx} - {lastz}*{lasty}")# print the following print message
    return s, -lastz# return the following coefficients

def question3():# format the question into one single functio#n
    sample = [(414,662), (6,14), (24,36), (12,42), (252,198)] # sample points that will be used in the sample
    print("--" * 40)# formatting
    for tup in sample:# iterating through all of the samples
        print("------------------------                      ")# formatting
        print(f'GCD({tup})')# formatting
        print("------------------------                      ")# formatting
        extended_gcd_steps(tup)# check the steps
        print("-------------------------------")
        print(f'backwards implementation: ')
        egcd_backwards(tup)
        print("------------------------                      ")# formatting
"""
Author combination: Yaeesh M. 
"""
def linear_combintation_extended_euclidean_algorithm(tup):
    s0= 1 # initilize the s0 vairbale
    s1 = 0# initilize the s1 vairbale
    t0 = 0 # initilizs the t0 variable
    t1 = 1# initilize the t1 variable

    x = max(tup)# find the max of the tuple
    y = min(tup)# find the min of the tuple
    a = max(tup)# find the max of the tuple
    b = min(tup)# find the min of the tuple
    quotiencoefficient_t_list =[]# create a qquotient list that will store variables
    while y!=0:# while the min of the tuple is not 0
        r = x%y# find the remainder of the two
        integer_division = x//y# find the int div of the two
        quotiencoefficient_t_list.append(integer_division)# append the int div to the list
        x=y# set x equal to y
        y=r# then set y equal to remainder
    gcd = return_gcd(tup)# find the gcd of the tuple
    coefficient_s_list= [1,0]# fill the list of the s coefficents with the current coefficents

    coefficient_t_list = [0,1]# fill the list of the t coefficents with the current coefficents

    for i in range(len(quotiencoefficient_t_list)-1):# iterate through the length of the t list
        s1 = s0-s1*quotiencoefficient_t_list[i]
        coefficient_s_list.append(s1) # add s1 to the variable list
        s0, s1 = s1, s0-s1*quotiencoefficient_t_list[i]# swap the values of the list
        t1 = t1*quotiencoefficient_t_list[i]# t1 equals this function
        coefficient_t_list.append(t1)# append to the list
        t0, t1 = t1, t0-t1*quotiencoefficient_t_list[i]# swap the values of the list
    for i in range(1,len(quotiencoefficient_t_list)+1):# iterate through needed iterations of the list
        print(f'q{i} = {quotiencoefficient_t_list[i-1]}, ', end="")# print the needed print message
    print("")# formatting
    print("s0= 1, s1= 0, ", end="")# print (formatting) needed language 
    for i in range(2,len(coefficient_s_list)):# iterate through the len of the coefficent 
        print(f's{i} = s{i-2} - s{i-1}*q{i-1} = {coefficient_s_list[i-2]} - {coefficient_s_list[i-1]}*{quotiencoefficient_t_list[i-2]} = {coefficient_s_list[i]}, ', end="")# print the following messages
    print("")# formatting for the print statements

    print("t0= 0, t1= 1, ", end="")# formatting for the print statements
    for i in range(2,len(coefficient_t_list)):# formatting for the print statements (itertions through the)
        print(f't{i} = t{i-2} - t{i-1}*q{i-1} = {coefficient_t_list[i-2]} - {coefficient_t_list[i-1]}*{quotiencoefficient_t_list[i-2]} = {coefficient_t_list[i]}, ', end="")
    print("")# formatting

    if s1*a + t1*b == x: # check if that combination of s and t; if this agrees, then the linear conbimation will work
        print(f"gcd({a}, {b}) = {s1}*{a} + {t1}*{b}")# print the combination
    else:# if this is not the case
        print(f"gcd({a}, {b}) = {t1}*{a} + {s1}*{b}")# print the other statement

def question4():# formatting for the question four; this takes all of the functions and places them in the same place
    sample = [(414,662), (6,14), (24,36), (12,42), (252, 198)]# sample points
    for tup in sample:# iterte through all of the elements in the sample
        print("--" * 40)# formatting
        linear_combintation_extended_euclidean_algorithm(tup)# call the function
        print("--" * 40)# formatting





def main():# create main function
    print("-"*40)# formatting
    print(f'Problem 1')# formatting
    print("-"*40)# formatting
    question1()# calling question 1
    print("-"*40)# formatting
    print(f'Problem 2')# formatting
    print("-"*40)# formatting
    question2()# calling question 2
    print("-"*40)# formatting
    print(f'Problem 3')# formatting
    print("-"*40)# formatting
    question3()# calling question 3
    print("-"*40)# formatting
    print(f'Problem 4') # formatting
    print("-"*40)# formatting
    question4()# formatting
    print("-"*40) # formatting
main()# call main function
