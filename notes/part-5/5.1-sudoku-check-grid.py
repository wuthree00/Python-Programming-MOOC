## Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument.
## The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly.
## Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid.
# If all contain each of the numbers 1 to 9 at most once, the function returns True.
# If a single one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders.
# These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

#-------------------------------------#
# sudoku1 = [                         #
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],      #
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],      #
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],      #
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],      #
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],      #
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],      #
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],      #
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],      #
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]       #
# ]                                   #
#                                     #
# print(sudoku_grid_correct(sudoku1)) #
#                                     #
# sudoku2 = [                         #
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],      #
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],      #
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],      #
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],      #
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],      #
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],      #
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],      #
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],      #
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]       #
# ]                                   #
#                                     #
# print(sudoku_grid_correct(sudoku2)) #
#-------------------------------------#
# Sample output:                      #
# False                               #
# True                                #
#-------------------------------------#


## Solution:
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no] #this sets each row to be referenced by the row number
    for i in range(1,10): #this means 'let i be each number from 1 to 9, one at a time'
        if row.count(i) > 1: #this means 'if number i appears more than once in this row'
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no]) #add the integer value at index column_no in that row, to the list called called column
    for i in range(1,10):
        if column.count(i) > 1: #if number i (which loops from 1 to 9) appears more than once in the column list
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    list_of_block_values = []
    #collect all the values in the 3x3 block into a list
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            list_of_block_values.append(sudoku[i][j])
    #for numbers 1-9, check if any appear more than once in the 3x3 block
    for number in range(1,10):
        if list_of_block_values.count(number) > 1:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    #check if all 9 rows are correct
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
    #check if all 9 columns are correct
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False
    #check if all 9 blocks are correct
    for row_no in [0,3,6]: #means let row_no be 0, then 3, then 6 (one at a time)
        for column_no in [0,3,6]: #means let column_no be 0, 3, 6 (one at a time)
            if not block_correct(sudoku, row_no, column_no):
                return False
    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))

