## Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes.
## The function takes an integer argument, which specifies the length of the side of the board.
# See the examples below for details:

#-------------#
# chessboard(3)
# print()
# chessboard(6)
#-------------#

## Sample output
# 101
# 010
# 101

# 101010
# 010101
# 101010
# 010101
# 101010
# 010101


## Solution:
def chessboard(n):
    for row in range(n):
        if row % 2 == 0:                   #if row is even like row 0, 2, 4
            print("10" * (n//2) + ("1" if n % 2 else ""))
        else:                              #if row is odd like row 1, 3, 5
            print("01" * (n//2) + ("0" if n % 2 else ""))

if __name__ == "__main__":
    chessboard(2)
