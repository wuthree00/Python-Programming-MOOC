### PART 4 ###

## NOTE: This exercise contains 4 parts,
## with each subsequent part building on the code used in the previous part

# I've separated my solution into 4 files corresponding with each part
## for easy reference and comparison of changes made to the functions defined in the solution


## Summary of database ##
#----------------------------------------------------------------------------------#
## Please write a function named summary,
## which prints out a summary based on all the information stored in the database.

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# This should print out:
# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza
#----------------------------------------------------------------------------------#


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

## Part 2 & 3
def add_course(students: dict, name: str, course: tuple):        
    if name in students and course[1] > 0: #if name is in dict and grade is > 0
        for i in range(len(students[name])): #means: run the loop once for each number
            #from 0 to (but not including) the length.
            #so it repeats the following code once for every course
            if students[name][i][0] == course[0]: #if course name already exists for this student
                if course[1] > students[name][i][1]: #if new grade > existing grade
                    students[name][i] = course #students[name][i] refers to the course tuple at position i
                return
        students[name].append(course) #if course name not in list, add course to list

## Part 4
def summary(students: dict):
    #to find no. of students in 'students' database (dictionary)
    no_of_students = len(students)
    print(f"students {no_of_students}")

    #to find the student with most completed courses
    most_courses = 0
    for name in students:
        if len(students[name]) > most_courses:
            most_courses = len(students[name])
            person_with_most_courses = name
    print(f"most courses completed {most_courses} {person_with_most_courses}")

    #to find the student with best average grade
    best_average = 0
    for name in students:
        total_grade = 0
        for course in students[name]:
            total_grade += course[1]
        average_grade = total_grade / len(students[name])
        if average_grade > best_average:
            best_average = average_grade
            person_with_best_average = name
    print(f"best average grade {best_average} {person_with_best_average}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)



## The model solution provided: ##
#----------------------------------------------------------------------------------#
# def add_student(students: dict, name: str):
#     students[name] = {}
# 
# def print_student(students: dict, name: str):
#     if not name in students:
#         print(f"{name}: no such person in the database")
#         return
# 
#     students_completed_courses = students[name]
# 
#     print(f"{name}:")
#     if len(students_completed_courses) == 0:
#         print(" no completed courses")
#     else:
#         print(f" {len(students_completed_courses):} completed courses:")
#         sum = 0
#         for course, grade in students_completed_courses.items():
#             course_grade = grade[1]
#             print(f"  {course} {course_grade}")
#             sum += course_grade
# 
#         print(f" average grade {sum/len(students_completed_courses):.1f}")
# 
# def add_course(students: dict, name: str, completion: tuple):
#     students_completed_courses = students[name]
#     course_name = completion[0]
#     course_grade = completion[1]
# 
#    # failed course is not recorded in the database
#     if course_grade==0:
#         return
# 
#    # if previous grade is higher, new grade is not recorded in the database
#     if course_name in students_completed_courses:
#         if students_completed_courses[course_name][1] > course_grade:
#             return
# 
#     students_completed_courses[course_name] = completion
# 
# def summary(students: dict):
#     print(f"students {len(students)}")
#     most_courses_count = 0
#     best_avg_grade = 0
#     for name, completions in students.items():
#         if len(completions) > most_courses_count:
#             most_courses = name
#             most_courses_count = len(students[most_courses])
# 
#         sum = 0
#         for course, grade in completions.items():
#             sum += grade[1]
# 
#         if len(completions)==0:
#             avg = 0
#         else:
#             avg = sum/len(completions)
# 
#         if avg>best_avg_grade:
#             best_avg_grade = avg
#             best = name
# 
#     print(f"most courses completed {most_courses_count} {most_courses}")
#     print(f"best average grade {best_avg_grade:.1f} {best}")
#----------------------------------------------------------------------------------#
