## NOTE: this was pretty tough and took me a few days to figure out!

## In this exercise you will write a program for printing out grade statistics for a university course.

# The program asks the user for results from different students on the course.
# These include exam points and numbers of exercises completed.
# The program then prints out statistics based on the results.

# Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

# The program keeps asking for input until the user types in an empty line.
# You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

# And example of how the data is typed in:

# Sample output
#---------------------------------------------
# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:
#---------------------------------------------

# When the user types in an empty line, the program prints out statistics.
# They are formulated as follows:

# The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth.
# Completing all 100 exercises grants 10 exercise points.
# The number of exercise points granted is an integer value, rounded down.

# The grade for the course is determined based on the following table:

#-------------|-----------------------
# exam points + exercise points	grade|
#-------------|-----------------------
# 0–14	      | 0 (i.e. fail)        |
# 15–17	      | 1                    |
# 18–20	      | 2                    |
# 21–23       | 3                    |
# 24–27	      | 4                    |
# 28–30	      | 5                    |
#-------------|-----------------------

# There is also an exam cutoff threshold.
# If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

# With the example input from above the program would print out the following statistics:

# Sample output
#------------------------
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *
#------------------------

# Floating point numbers should be printed out with one decimal precision.

# NB: this exercise doesn't ask you to write any specific functions, so you should not place any code within an if __name__ == "__main__" block.
# If any functionality in your program is e.g. in the main function, you should include the code calling this function normally, and not contain it in an if block like in the exercises which specify certain functions.

# Hint: The user input in this program consists of lines with two integer values:

# Sample output
# Exam points and exercises completed: 15 87

# You have to first split the input line in two and then convert the sections into integers with the int function.
# Splitting the input can be achieved in the same way as in the exercise First, second and last words, but there is a simpler way as well.
# The string method split will chop the input up nicely.
# You will find more information by searching for python string split online.



## Solution
total_exam_points = [] #A
total_exercise_points = [] #B
grades = [] #C
    
def user_input():
    raw_input = input("Exam points and exercises completed: ")
    return raw_input

def exam_points(inputted):
    i = inputted.split(" ") #.split splits the input into a list of strings
    total_exam_points.append(int(i[0])) #EACH student's exam points gets added to the total_exam_points list
    return int(i[0]) #but only this particular student's exam points is returned

def exercise_points(inputted):
    i = inputted.split(" ")
    each_exercise_points = int(i[1])//10
    total_exercise_points.append(each_exercise_points) #EACH student's exercises completed gets added to the total_exercises_completed list
    return each_exercise_points #but only this particular student's exercises completed is returned

def grade(exam_points, exercise_points): #this calculates the grade of ONE student
    total_points = exam_points + exercise_points
    if exam_points < 10:
        return 0
    elif total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 28:
        return 4
    else:
        return 5

def main():
    while True:
        the_input = user_input()
        if the_input == "":
            break
        actual_exam_points = exam_points(the_input) #calculates the exam points for THIS particular student, adding it to total_exam_points list and returns (not prints) it
        actual_exercise_points = exercise_points(the_input) #calculates the exercise points for THIS particular student, adding it to total_exercise_points list and returns (not prints) it
        actual_grade = grade(actual_exam_points, actual_exercise_points) #calculates the grade for THIS particular student, returning (not printing) it
        grades.append(actual_grade) #EACH student's grade gets added to the grades list

    print("Statistics:")
    print(f"Points average: {(sum(total_exam_points) + sum(total_exercise_points))/len(grades)}")
    number_of_fails = grades.count(0)
    number_of_passes = len(grades) - number_of_fails
    print(f"Pass percentage: {number_of_passes/len(grades)*100:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1): #from 5 to 0, backwards (the first -1 has to be one less than the last number (which is 0) becos the last number is NOT included in the range)
        print(f"{i}: {'*' * grades.count(i)}") #print the grade, then the number of times the grade appears in the grades list, each represented by an asterisk

main()
