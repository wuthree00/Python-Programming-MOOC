## Please write a program which asks the user for a positive integer N.
## The program then prints out all numbers between -N and N inclusive, but leaves out the number 0.
## Each number should be printed on a separate line.

# An example of expected behaviour:

## Sample output:
#--------------------------------------
# Please type in a positive integer: 4
# -4
# -3
# -2
# -1
# 1
# 2
# 3
# 4
#--------------------------------------


## Solution:
N = int(input("Please type in a positive integer: "))    
for i in range(-N, 0, 1):
    print(i)
for i in range(1, N+1, 1):
    print(i)
