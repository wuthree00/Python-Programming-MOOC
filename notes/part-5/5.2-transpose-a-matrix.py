## Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument.
## The function should transpose the matrix.
## Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

# The following matrix
# 1 2 3
# 4 5 6
# 7 8 9

# transposed looks like this:
# 1 4 7
# 2 5 8
# 3 6 9

# The function should not have a return value.
# The matrix should be modified directly through the reference.


## Solution:
def transpose(matrix: list):
    n = len(matrix) #the number of rows/columns
    temporary_matrix = [] #1. create a temporary list to hold the transposed values b4 copying them directly into original matrix
    for column in range(n): #for each column, running from 0 to 2 (3 columns) one by one
        new_row = [] #each column needs to become a new row in the transposed matrix!
        for row in range(n): #now that the column is fixed (at 0 for eg), loop thru each row 0 to 2 (3 rows) one by one
            new_row.append(matrix[row][column]) #col no. is fixed, only row changes here. so for col 0, we are appending matrix[0][0], matrix[1][0], matrix[2][0] into the FIRST sublist in temporary_matrix. repeats for each column
        temporary_matrix.append(new_row) #append each new sublist (which is a list of 3 values from each COLUMN) to temporary_matrix
    
    #2. now, copy the transposed values from temporary_matrix back into original matrix
    matrix[:] = temporary_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transpose(matrix)
    print(matrix)


## Model solution provided:
# def transpose(matrix: list):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i, n):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp
 
            #..or alternatively
            # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
