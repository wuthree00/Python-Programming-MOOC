### PART 1 ###

## NOTE: This exercise contains 4 parts,
## with each subsequent part building on the code used in the previous part

# I've separated my solution into 4 files corresponding with each part
## for easy reference and comparison of changes made to the functions defined in the solution


## Adding students ##
#---------------------------------------------------------------------------------------#
## First write a function named add_student, which adds a new student to the database.
## Also write a preliminary version of the function print_student,
## which prints out the information of a single student.

# These functions are used as follows:
# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")

# Your program should now print out:
# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database
#---------------------------------------------------------------------------------------#


## Solution:
def add_student(students: dict, name: str):
    students[name] = [] #add name to the dictionary called students, and set the value as an empty list (for use later)


def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}: \n no completed courses")
    else:
        print(f"{name}: no such person in the database")
        
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
