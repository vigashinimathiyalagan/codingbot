mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

if mark1 == 100 or mark2 == 100 or mark3 == 100:
    print("Grade A")
elif mark1 >= 90 or mark2 >= 90 or mark3 >= 90:
    print("Grade B")
elif mark1 >= 60 or mark2 >= 60 or mark3 >= 60:
    print("Grade C")
elif mark1 <= 50 and mark2 <= 50 and mark3 <= 50:
    print("Grade F")
else:
    print("Grade D")
output:
  Enter mark 1: 100
Enter mark 2: 100
Enter mark 3: 100
Grade A
Enter mark 1: 90
Enter mark 2: 90
Enter mark 3: 90
Grade B
Enter mark 1: 50
Enter mark 2: 50
Enter mark 3: 50
Grade F
