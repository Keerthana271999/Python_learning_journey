from math import ceil

# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

'''
number of students on a course - number of students enrolled to a (single) course
desired group size = how many are expected to be formed
'''
students = int(input("Number of students enrooled to a course: "))
group_size = int(input("Desired group size: "))
try:
    formed = students/group_size
    print("Number of groups formed per course:", ceil(formed))
except ZeroDivisionError as msg:
    print(f"Error: {msg.__class__.__name__}")
    print(f"Details: {msg}")
