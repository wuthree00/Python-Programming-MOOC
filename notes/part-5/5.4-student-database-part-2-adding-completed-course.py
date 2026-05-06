### PART 2 ###

## NOTE: This exercise contains 4 parts, with each subsequent part building on the code used in the previous part ##

# I've separated my solution into 4 files corresponding with each part for easy reference and comparison of changes made to the functions defined in the solution


## Adding completed course ##
#-----------------------------------------------------------------------------------------#
## Please write a function named add_course,
## which adds a completed course to the information of a specific student in the database.
## The course data is a tuple consisting of the name of the course and the grade:

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")
# When some courses have been added, the information printed out changes:

# Sample output
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5
#-----------------------------------------------------------------------------------------#


## Solution:
## Part 1
def add_student(students: dict, name: str):
    students[name] = [] #add name to the dictionary called students, and set the value as an empty list (for later use)

def print_student(students: dict, name: str):
    if name in students:
        if students[name]: #if value of students[name] is not empty
            print(f"{name}: \n {len(students[name])} completed courses:")
            for course in students[name]:
                print(f"  {course[0]} {course[1]}")
            for i in range(len(students[name])):
                total_grade = 0
                for course in students[name]:
                    total_grade += course[1]
                average_grade = total_grade / len(students[name])
            print(f" average grade {average_grade}")           
        else:print(f"{name}: \n no completed courses")
    else:
        print(f"{name}: no such person in the database")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")


## Part 2
def add_course(students: dict, name: str, course: tuple):
    if name in students:
        students[name].append(course)
## now edit print_student in part 1

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
