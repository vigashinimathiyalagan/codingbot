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

marksInMaths = [56, 78, 56, 45, 90]
avgMaths = sum(marksInMaths) / len(marksInMaths)

marksInScience = [90, 78, 67, 8, 98]
avgScience = sum(marksInScience) / len(marksInScience)

marksInHistory = [87, 44, 56, 34, 90]
avgHistory = sum(marksInHistory) / len(marksInHistory)

#Call divide function to get the average from all three subjects
avg = divideAFromB(3, avgMaths + avgScience + avgHistory)

print("The avg mark is", avg)
output:
  The avg mark is 65.13333333333333
