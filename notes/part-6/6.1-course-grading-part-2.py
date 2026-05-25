## Let's expand the program created in the previous exercise.
## Now also the exam points awarded to each student are contained in a CSV file.
## The contents of the file follow this format:

# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2

# In the above example the student whose student number is 12345678 was awarded
# 4+1+4 points in the exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files.
# Then the program should process the files and print out a grade for each student.

# Sample output
#-------------------------------------#
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3
#-------------------------------------#

# Each completed exercise is counted towards exercise points,
# so that completing at least 10 % of the total exercices awards 1 point,
# completing at least 20 % awards 2 points, etc.
# Completing all 40 exercises awards 10 points.
# The number of points awarded is always an integer number.

# The final grade for the course is determined based on the
# sum of exam and exercise points according to the following table:

# exam points + exercise points	|  grade
#            0-14               |  0 (fail)
#            15-17              |  1
#            18-20              |  2
#            21-23              |  3
#            24-27              |  4
#            28-                |  5

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.



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
    print(f"{names[id]} {final_grade}")

#grade = exam points (total of all exams) + exercise points (calculated by % of exercises completed)
#total no. of exercises = 40
#exercise points:
#0-9% of 40 exercises = 0 points
#10-19% of 40 exercises = 1 point
#20-29% of 40 exercises = 2 points
#30-39% of 40 exercises = 3 points
#40-49% of 40 exercises = 4 points
#50-59% of 40 exercises = 5 points
#60-69% of 40 exercises = 6 points
#70-79% of 40 exercises = 7 points
#80-89% of 40 exercises = 8 points
#90-99% of 40 exercises = 9 points
#100% of 40 exercises = 10 points



## Model solution provided:
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
 
# for student_id, name in students.items():
#     total = exams[student_id] + to_points(exercises[student_id])
#     print(f"{name} {grade(total)}")
