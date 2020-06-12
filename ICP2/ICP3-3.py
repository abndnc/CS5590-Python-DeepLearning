myFile = open("sample.txt", "r")
myDict = {}
line = myFile.readline()
while line != "":
    mylist = line.split()
    for i in mylist:
        if i not in myDict:
            myDict[i] = 1
        else:
            myDict[i] += 1
    line = myFile.readline()

myFile.close()


with open('sample.txt', 'a') as f:
    f.write("\n")
    print(myDict, file=f)