## Please write a function named print_many_times(text, times), which takes a string and an integer as arguments.
## The integer argument specifies how many times the string argument should be printed out:

#-------------------------------------------#
# print_many_times("hi", 5)
#
# print()
#
# text = "All Pythons, except one, grow up"
# times = 3
# print_many_times(text, times)
#-------------------------------------------#

## Sample output
# hi
# hi
# hi
# hi
# hi

# All Pythons, except one, grow up.
# All Pythons, except one, grow up.
# All Pythons, except one, grow up.


## Solution:
def print_many_times(text, times):
    count = 0
    while count < times:
        print(text)
        count += 1

# Test the function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
