inputString = input("Enter a string: ")
i = 0
newString = ""

while i < len(inputString):
    newString += inputString[i:i+2]  
    newString += " " 
    i += 2


if i < len(inputString):
    newString += inputString[i:]

print(newString)

