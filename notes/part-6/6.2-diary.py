## Please write a program which works as a simple diary.
## The diary entries should be saved in the file diary.txt.
## When the program is executed, it should first read any entries already in the file.

# NB: the automatic tests for this exercise will change the contents of the file.
# If you want to keep its contents, first make a copy of the file under a different name.

# The program should work as follows:
#----------------------------------------------------#
# Sample output:
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!
#----------------------------------------------------#


# When the program is executed for the second time, this should happen:
#----------------------------------------------------#
# Sample output:
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!
#----------------------------------------------------#

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.


## My solution:
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")

    if function == "1":
        diary_entry = input("Diary entry:")
        with open("diary.txt", "a") as new_file:
            new_file.write(f"{diary_entry}\n")
        print("Diary saved\n")

    elif function == "2":
        print("Entries:")
        with open("diary.txt") as new_file:
            for line in new_file:
                print(line, end="")

    elif function == "0":
        print("Bye now!")
        break


## Model solution provided:
# Read the markings first
# with open("diary.txt") as file:
#     content = []
#     for row in file:
#         content.append(row.replace("\n",""))
 
# Open file for appending
# with open("diary.txt", "a") as file:
#     while True:
#         print("1 - add an entry, 2 - read entries, 0 - quit")
#         function = input("Function: ")
#         if function == "1":
#             entry = input("Diary entry: ")
#             file.write(entry + "\n")
#             content.append(entry)
#             print("Diary saved")
#         elif function == "2":
#             print("Entries:")
#             for entry in content:
#                 print(entry)
#         elif function == "0":
#             print("Bye now!")
#             break
