## The file numbers.txt contains integer numbers, one number per line.
## The contents could look like this
# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...

# Please write a function named largest,
# which reads the file and returns the largest number in the file.

# Notice that the function does not take any arguments.
# The file you are working with is always named numbers.txt.


## Solution:
def largest():
    with open("numbers.txt") as new_file:
        numbers = []
        for line in new_file:
            numbers.append(int(line)) #this appends each line as an int to the list 'numbers'
        return max(numbers)

if __name__ == "__main__":
    print(largest())


## The model solution provided:
# def largest():
#     with open("numbers.txt") as file:
#         start = True
#         biggest = 0
#         for number in file:
#             if start or int(number) > biggest:
#                 biggest = int(number)
#                 start = False
#         return biggest


