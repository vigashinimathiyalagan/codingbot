#This code has functions for basic arithmetic operations: add, subtract, multiply, and divide.
#The main function adds all student marks and finds the average.

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans

def subtractAfromB(a, b):
    ans = a - b
    return ans

def multiplyTwoNumbers(n1, n2):
    ans = n1 * n2
    return ans

def divideAFromB(a, b):
    ans = b / a
    return ans

#main code

#Get 5 marks from student and find the total
total = 0
for i in range(1, 6):
    mark = int(input("Enter mark " + str(i) + ": "))
    total = addTwoNumbers(total, mark)

#Call divide function to get the average
avg = divideAFromB(5, total)

print("The average mark is", avg)

output:
  Enter mark 1: 99
Enter mark 2: 100
Enter mark 3: 100
Enter mark 4: 78
Enter mark 5: 89
The average mark is 93.2



