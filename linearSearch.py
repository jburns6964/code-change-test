testString = ""
searchChar = ""
charList = []
lastPosition = -1

while testString == "":
    testString = input("Please enter some text to search : ")
    str.lower(testString)

while len(searchChar) != 1:
    searchChar = input("Enter a character to search for :")

for x in range (len(testString)):
    if testString[x] == searchChar:
        charList.append(x-lastPosition)
        lastPosition = x

if searchChar == str.lower(searchChar):
    searchChar = str.capitalize(searchChar)
elif searchChar == str.capitalize(searchChar):
    searchChar = str.lower(searchChar)    

for x in range (len(testString)):
    if testString[x] == searchChar:
        charList.append(x-lastPosition)
        lastPosition = x

if searchChar == str.lower(searchChar):
    searchChar = str.capitalize(searchChar)
elif searchChar == str.capitalize(searchChar):
    searchChar = str.lower(searchChar)   

print ("I found {0} occurences of {1}".format(len(charList),searchChar))

