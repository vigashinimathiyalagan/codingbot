#problem 1


tamilMark = int(input("Enter Tamil mark: "))
englishMark = int(input("Enter English mark: "))
totalMarks = tamilMark + englishMark
passmark = 35

# Pass condition
if (tamilMark >= 95 or englishMark >= 95):
    print("Pass")

# First Class conditions
if (tamilMark > 85 and englishMark > 65) or (tamilMark > 65 and englishMark > 85):
    print("First Class")

if (tamilMark >= 70 and tamilMark <= 90) and (englishMark >= 50 and englishMark <= 70):
    print("First Class")

# Fail condition
if tamilMark < passmark or englishMark < passmark:
    print("Fail")

output:
  Enter Tamil mark: 88
Enter English mark: 90
First Class
Enter Tamil mark: 95
Enter English mark: 95
Pass
First Class
Enter Tamil mark: 75
Enter English mark: 65
First Class
Enter Tamil mark: 35
Enter English mark: 34
Fail
#problem 2
tamilMark = int(input("Enter Tamil mark: "))
englishMark = int(input("Enter English mark: "))
passmark = 35

if tamilMark >= passmark and englishMark >= passmark:
    print("Pass")
else:
    if tamilMark < passmark:
        print("Failed in Tamil")
    else:
        print("Failed in English")
        
        
 output:
  Enter Tamil mark: 37
Enter English mark: 38
Pass
Enter Tamil mark: 78
Enter English mark: 34
Failed in English
Enter Tamil mark: 35
Enter English mark: 99
Pass
Enter Tamil mark: 33
Enter English mark: 99
Failed in Tamil

#problem 3
tamilMark = int(input("Enter Tamil mark: "))
englishMark = int(input("Enter English mark: "))
passmark = 35
totalMarks = tamilMark + englishMark
if tamilMark >= passmark and englishMark >= passmark:
    print("Pass")
elif totalMarks >= 90 and tamilMark >= 25 and englishMark >= 25:
    print("Pass")
else:
    print("Fail")

    
    output:
      Enter Tamil mark: 67
Enter English mark: 90
Pass
Enter Tamil mark: 60
Enter English mark: 30
Pass
Enter Tamil mark: 25
Enter English mark: 25
Fail
Enter Tamil mark: 45
Enter English mark: 23
Fail
Enter Tamil mark: 23
Enter English mark: 89
Fail

