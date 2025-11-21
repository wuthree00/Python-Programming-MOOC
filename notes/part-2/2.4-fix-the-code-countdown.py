## This program should print out a countdown. The code is as follows:

## | number = 5
## | print("Countdown!")
## | while True:
## |   print(number)
## |   number = number - 1
## |   if number > 0:
## |     break
## | 
## | print("Now!")

# This should print out:

## Sample output
# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!

# However, the program doesn't quite work. Please fix it.


## Solution:
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number == 0:
    break

print("Now!")


##### The PROBLEM:
# the condition "if number > 0:
#                  break"
# caused the program to stop running right after printing the first number, which was 5, as it was greater than 0
# as a result, the loop ended prematurely

##### My solution was the change > to ==, so that the loop only breaks when the integer printed reaches 1!
