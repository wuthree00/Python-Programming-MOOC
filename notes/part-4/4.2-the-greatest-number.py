## Please write a function named greatest_number, which takes three arguments.
## The function returns the greatest in value of the three.

# An example of how the function is used:
# print(greatest_number(3, 4, 1)) # 4
# print(greatest_number(99, -4, 7)) # 99
# print(greatest_number(0, 0, 0)) # 0


## Solution:
def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c

# Test the function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(0, 0, 0)
    print(greatest)
