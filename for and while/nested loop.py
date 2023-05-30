# for student in range(3):
#     student_name = input("Enter student name: ")
#     for mark in range(2):
#         input_mark = float(input(f"Enter mark {mark+1} for {student_name}: "))
#         print(f"Mark {mark+1} for {student_name} is {input_mark}")

# # Problem 1.1
for student in range(3):
    student_name = input("Enter student name: ")
    marks = []
    for mark in range(2):
        input_mark = float(input(f"Enter mark {mark+1} for {student_name}: "))
        marks.append(str(input_mark))
    print(f"{student_name}'s marks: {', '.join(marks)}")
output:

Enter student name: shini
Enter mark 1 for shini: 57
Enter mark 2 for shini: 89
shini's marks: 57.0, 89.0
Enter student name: viga
Enter mark 1 for viga: 89
Enter mark 2 for viga: 90
viga's marks: 89.0, 90.0
Enter student name: haritha
Enter mark 1 for haritha: 89
Enter mark 2 for haritha: 90
haritha's marks: 89.0, 90.0


