numS = input("Please enter the number of students: ") # get the number of students from user
numS = int(numS)
weightlist = [] # list of lbs weight
kglist = [] # list of kg weight
for n in range(numS):
    weight = input("Please enter the student weight(lbs): ") # get the lbs weight
    weight = int(weight) # convert the input to integer
    weightlist.append(weight) # add the lbs weight to the list
    kglist.append(weight*0.453592) # add the converted kg weight to the list
print("List of the student's weight:")
for n in range(numS): # print out result
    print("Student ", n+1, " weights ", kglist[n], " kg.")
input("Press enter to exit.")