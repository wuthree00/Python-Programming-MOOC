## Exercise: Grades and points

## The table below outlines the grade boundaries on a certain university course.
## Write a program which asks for the amount of points received and prints out the grade attained according to the table.

# +---------+--------------+
# | points  |    grade     |
# +---------+--------------+
# |  < 0    | impossible!  |
# | 0–49    | fail         |
# | 50–59   | 1            |
# | 60–69   | 2            |
# | 70–79   | 3            |
# | 80–89   | 4            |
# | 90–100  | 5            |
# |  > 100  | impossible!  |
# +---------+--------------+

## Sample output
# How many points [0-100]: 37
# Grade: fail

## Sample output
# How many points [0-100]: 76
# Grade: 3

## Sample output
# How many points [0-100]: -3
# Grade: impossible!


## Solution:
points = int(input("How many points [0-100]:"))

if points < 0 or points > 100:
    print("Grade: impossible!")

elif 0 <= points < 50:
    print("Grade: fail")
elif 50 <= points < 60:
    print("Grade: 1")
elif 60 <= points < 70:
    print("Grade: 2")
elif 70 <= points < 80:
    print("Grade: 3")
elif 80 <= points < 90:
    print("Grade: 4")
elif 90 <= points <= 100:
    print("Grade: 5")
