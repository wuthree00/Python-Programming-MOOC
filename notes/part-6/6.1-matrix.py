## The file matrix.txt contains a matrix in the format specified in the example below:
# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc…

## Please write two functions, named matrix_sum and matrix_max.
## Both go through the matrix in the file,
## and then return the sum of the elements or the element with the greatest value,
## as the names of the functions imply.

# Please also write the function row_sums,
# which returns a list containing the sum of each row in the matrix.
# For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4
# The function should return the list [6, 9].

# Hint: you can also include other helper functions in your program.
# It is very worthwhile to spend a moment considering which functionalities
# are shared by the three functions you are asked to write.
# Notice that the three functions named above do not take any arguments,
# but any helper functions you write may take arguments.
# The file you are working with is always named matrix.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors,
# take a look at the instructions before this exercise.


## Solution:
def read_matrix():
    #this function reads the matrix from the file and returns it as a list of lists (where each list contains the numbers)
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file: #go line by line
            line = line.replace("\n", "") #remove the invisible newline character at end of each line
            parts = line.split(",") #split each line into parts by comma
            row = [] #now, each line is split into parts. create a list for each line, each will be a row in the matrix
            for part in parts: #each "part" is the number in each line (but note the numbers are still strings, not integers)
                number = int(part) #convert each individual part into integer
                row.append(number) #add each number (now an integer) to the row one by one
            matrix.append(row) #after forming each row with numbers, add each row to the matrix one by one
        return matrix
    
#note the matrix looks like this:
# matrix = [
#     [1, 0, 2, 8, ...],
#     [9, 2, 4, 5, ...],
#     [...]
# ]

def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix: #this runs thru all the rows, one by one
        total += sum(row) #this adds the sum of each row to the total
    return total


def matrix_max():
    matrix = read_matrix()
    largest = matrix[0][0] #use first value in matrix as starting value.
    #using 0 would fail if all numbers in the matrix are negative!
    for row in matrix: #loop thru each row, one by one
        row_max = max(row)
        if row_max > largest:
            largest = row_max #this updates largest if this row contains a bigger value
    return largest


def row_sums():
    matrix = read_matrix()
    sum_of_rows = []
    for row in matrix: #loop thru each row
        sum_of_rows.append(sum(row)) #find sum of each row, add it to the new list
    return sum_of_rows


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())



## The model solution provided:
# def read_matrix():
#     with open("matrix.txt") as file:
#         m = []
#         for row in file:
#             mrow = []
#             items = row.split(",")
#             for item in items:
#                 mrow.append(int(item))
#             m.append(mrow)
# 
#     return m
# 
# Yhdistää matriisin rivit yhdeksi listaksi
# def combine(matriisi: list):
#     mlist = []
#     for row in matriisi:
#         mlist += row
#    
#     return mlist
# 
# def matrix_sum():
#     mlist = combine(read_matrix())
#     return sum(mlist)
# 
# def matrix_max():
#     mlist = combine(read_matrix())
#     return max(mlist)
# 
# def row_sums():
#     matrix = read_matrix()
#     sums = []
#     for row in matrix:
#         sums.append(sum(row))
#     return sums
