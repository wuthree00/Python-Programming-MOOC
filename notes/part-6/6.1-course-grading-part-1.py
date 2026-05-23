## This program works with 2 CSV files. One contains information about some students on a course:

# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder

# The other contains the number of exercises each student has completed each week:

# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2

# As you can see, both CSV files also have a header row,
# which tells you what each column contains.

# Please write a program which asks the user for the names of these two files,
# reads the files, and then prints out the total number of exercises completed by each student.
# If the files have the contents in the examples above,
# the program should print out the following:

# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35 

# Hint: while testing your program, you may quickly run out of patience
# if you always have to type in the file names at the prompt.
# You might want to hard-code the user input, like so:

# if False:
    # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
    # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

# The actual functionality of the program is now "hidden" in the False branch of an if statement.
# It will never be executed.

# Now, if you want to quickly verify the program works correctly also with user input,
# you can just replace False with True:

# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
    # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

# When you have verified your program works correctly,
# you can remove the if structure, keeping the commands asking for input.

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.


## My solution:
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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
        for i in range(1, len(parts)): #add each exercise integer to dictionary. dict is exercises, key is id which is parts[0]
            exercises[parts[0]].append(int(parts[i])) #add each exercise score to the list of exercises for this student))
        #dictionary: exercises[id] = [ex1, ex2, ex3...]
            
for id, name in names.items():
    print(name + " " + str(sum(exercises[id])))
