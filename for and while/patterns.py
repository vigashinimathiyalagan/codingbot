def draw_rectangle(row, column):
    for i in range(row):
        for j in range(column):
            if i == 0 or i == row - 1 or j == 0 or j == column - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Get width and length from the user
row = int(input("Enter the row of the rectangle: "))
column= int(input("Enter the column of the rectangle: "))

# Draw the rectangle
draw_rectangle(row, column)

output:
  Enter the row of the rectangle: 5
Enter the column of the rectangle: 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *
