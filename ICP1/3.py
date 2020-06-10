astring = input("Please type a sentence: ") # get input
if astring.count("python") > 0: # check if the sentence includes python
    astring = astring.replace("python", "pythons", astring.count("python")) # modify the word "python"
    print(astring)
else: # do nothing if there's no python counted
    print(astring) #
print("Thank you for using the program.")
input("Press enter to exit")
