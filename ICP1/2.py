# part 1
astring = input("Please type 'python': ") # get input from user
counter = 0 # a counter for the number of time we remove a character of the string
while counter != 2:
    astring = astring[:3] + astring[4:] # remove a character using slicing method
    counter = counter + 1
print("The output is ", astring[::-1]) # print the modified output

# part 2
num1 = input("Please type the first number: ") # get input from user
num1 = int(num1) # convert input into integer
num2 = input("Please type the second number: ")
num2 = int(num2)
print(num1, " plus ", num2, " equals ", num1+num2) # print the result of arithmetic operation
print(num1, " minus ", num2, "equals ", num1-num2)
print("Thank you for using the program.")
input("Press enter to exit")
