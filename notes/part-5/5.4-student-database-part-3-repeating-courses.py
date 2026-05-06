### PART 3 ###

## NOTE: This exercise contains 4 parts,
## with each subsequent part building on the code used in the previous part

# I've separated my solution into 4 files corresponding with each part
## for easy reference and comparison of changes made to the functions defined in the solution


## Repeating courses ##
#-------------------------------------------------------------------------------------------------#
## Courses with grade 0 should be ignored when adding course information.
## Additionally, if the course is already in the database in that specific student's information,
## the grade recorded in the database should never be lowered if the course is repeated.

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")

# Sample output
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5
#-------------------------------------------------------------------------------------------------#


## Solution:
## Part 1
def add_student(students: dict, name: str):
    students[name] = [] #add name to the dictionary called students,
                        #and set the value as an empty list (for later use)

def print_student(students: dict, name: str):
    if name in students:
        if students[name]: #if value of students[name] is not empty
            print(f"{name}: \n {len(students[name])} completed courses:")
            for course in students[name]:
                print(f"  {course[0]} {course[1]}")
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

## Part 2 & 3
def add_course(students: dict, name: str, course: tuple):        
    if name in students and course[1] > 0: #if name is in dict and grade is > 0
        for i in range(len(students[name])): #means: run the loop once for each number
                                             #from 0 to (but not including) the length
            #so it repeats the following code once for every course
            if students[name][i][0] == course[0]: #if course name already exists for this student
                if course[1] > students[name][i][1]: #if new grade > existing grade
                    students[name][i] = course #students[name][i] refers to the course tuple at position i
                return
        students[name].append(course) #if course name not in list, add course to list
## now edit print_student in part 1

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")
