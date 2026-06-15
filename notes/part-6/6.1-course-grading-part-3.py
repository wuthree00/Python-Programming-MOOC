## This exercise will continue from the previous one.
## Now we shall print out some statistics based on the CSV files.

# Sample output
#------------------------------------------------------------------------------#
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
#
# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
#------------------------------------------------------------------------------#

# Each row contains the information for a single student.
# The number of exercises completed, the number of exercise points awarded,
# the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns.
# The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

# You might find the f-strings covered in part 4 useful here.

# F-strings differentiate between strings and numbers when it comes to justifying columns:
#--------------------------------#
# word = "python"
# print(f"{word:10}continues")
# print(f"{word:>10}continues")
#--------------------------------#

# Sample output
#--------------------------------#
# python    continues
#     pythoncontinues
#--------------------------------#

# As you can see above, by default strings are justified to the left edge of the area specified for them.
# The > symbol can be used to justify to the right edge.

# With number values the logic is reversed:
#--------------------------------#
# number = 42
# print(f"{number:10}continues")
# print(f"{number:<10}continues")
#--------------------------------#

# Sample output
#--------------------------------#
#         42continues
# 42        continues
#--------------------------------#

# With numbers the default behaviour is to justify to the right edge.
# The symbol < can be used to justify to the left edge.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.


## My solution:
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

names = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2] #parts[0] is the id, parts[1] + parts[2] is the name (key-value pairs)
        #dictionary: names[id] = name

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exercises[parts[0]] = []
        for i in range(1, len(parts)): #add each exercise integer to the list of exercises for this student (list is the value of the dictionary)
            exercises[parts[0]].append(int(parts[i])) #add no. of exercises completed to the list of exercises for this student
        #dictionary: exercises[id] = [ex1, ex2, ex3...]

exams = {}
with open(exam_points) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exams[parts[0]] = []
        for i in range(1, len(parts)):
            exams[parts[0]].append(int(parts[i])) #add each exam score to the list of exam score for this student
        #dictionary: exams[id] = [exam1, exam2, exam3...]

def exercise_points(id):
    total_exercises = 40
    total_completed = sum(exercises[id])
    percentage_completed = total_completed / total_exercises
    if percentage_completed < 0.1:
        exercise_pt = 0
    elif percentage_completed < 0.2:
        exercise_pt = 1
    elif percentage_completed < 0.3:
        exercise_pt = 2
    elif percentage_completed < 0.4:
        exercise_pt = 3
    elif percentage_completed < 0.5:
        exercise_pt = 4
    elif percentage_completed < 0.6:
        exercise_pt = 5
    elif percentage_completed < 0.7:
        exercise_pt = 6
    elif percentage_completed < 0.8:
        exercise_pt = 7
    elif percentage_completed < 0.9:
        exercise_pt = 8
    elif percentage_completed < 1.0:
        exercise_pt = 9
    else:
        exercise_pt = 10
    return exercise_pt

print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")


for id, exam_scores in exams.items(): #key is id, value is list of exam scores
    grade = sum(exam_scores) + exercise_points(id)
    if grade < 15:
        final_grade = 0
    elif grade < 18:
        final_grade = 1
    elif grade < 21:
        final_grade = 2
    elif grade < 24:
        final_grade = 3
    elif grade < 28:
        final_grade = 4
    else:
        final_grade = 5
    exec_nbr = sum(exercises[id])
    exec_pts = exercise_points(id)
    exm_pts = sum(exam_scores)
    tot_pts = exec_pts + exm_pts
    print(f"{names[id]:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{final_grade:<10}")


## The model solution provided:
# student_data = input("Student information: ")
# exercise_data = input("Exercises completed: ")
# exam_data = input("Exam points: ")
 
# def grade(points):
#     a = 0
#     limits = [15, 18, 21, 24, 28]
#     while a < 5 and points >= limits[a]:
#         a += 1
 
#     return a

# def to_points(number):
#     return number // 4
 
# students = {}
# with open(student_data) as file:
#     for row in file:
#         parts = row.split(";")
#         if parts[0] == "id":
#             continue
#         students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
# exercises = {}
# with open(exercise_data) as file:
#     for row in file:
#         parts = row.split(";")
#         if parts[0] == "id":
#             continue
#         esum = 0
#         for i in range(1, 8):
#             esum += int(parts[i])
#         exercises[parts[0]] = esum
 
# exams = {}
# with open(exam_data) as file:
#     for row in file:
#         parts = row.split(";")
#         if parts[0] == "id":
#             continue 
#         esum = 0
#         for i in range(1, 4):
#             esum += int(parts[i])
#         exams[parts[0]] = esum
 
# print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
# for eid, name in students.items():
#     exec_nbr = exercises[eid]
#     exec_score = to_points(exec_nbr)
#     exam_points = exams[eid]
#     total_points = exec_score + exam_points
#     print(f"{name:30}{exec_nbr:<10}{exec_score:<10}{exam_points:<10}{total_points:<10}{grade(total_points):<10}")
