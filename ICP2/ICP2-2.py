def string_alternative(astring): # define a function
    for n in range(len(astring)): # loop with the length of the string
        if n % 2 == 0: # check if the index is in odd position
            print(astring[n], end ="") # print in the same line

astring = input('Please give input: ') # get input from user
string_alternative(astring) # assign the variable to the function
input("\nPress enter to exit: ")