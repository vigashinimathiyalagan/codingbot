#This code has functions for basic arithmetic operations: add, subtract, multiply, and divide.
#You can add new functions as needed.
#The main function is to find the total profit.

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

#we have sales data for a week.
costOfCoffee, costOfTea, costOfVadai = 25, 20, 25

coffeeSales = [56, 78, 56, 45, 90, 103, 120]
teaSales = [100, 123, 456, 123, 222, 400, 346]
vadaiSales = [23, 45, 67, 12, 89, 90, 120]

#Find total sales in the week.
totalSales = sum(coffeeSales) + sum(teaSales) + sum(vadaiSales)

#calculate avg sales for a week
avgSalesPerWeek = totalSales / 7

employeeSalary = 500 #Rs500 per day

#calculate sales per month
salesPerMonth = totalSales * 4

#calculate profit
totalCost = (costOfCoffee + costOfTea + costOfVadai) * 7
totalSalary = employeeSalary * 7
profit = totalSales - totalCost - totalSalary

print("The profit is", profit)

output:
  The profit is -1226
