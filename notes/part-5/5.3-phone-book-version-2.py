## Please write an improved version of the phone book application.
## Each entry should now accommodate multiple phone numbers.
## The application should work otherwise exactly as above,
## but this time all numbers attached to a name should be printed.

# Sample output
#--------------------------------------#
# command (1 search, 2 add, 3 quit): 2 #
# name: peter                          #
# number: 040-5466745                  #
# ok!                                  #
# command (1 search, 2 add, 3 quit): 2 #
# name: emily                          #
# number: 045-1212344                  #
# ok!                                  #
# command (1 search, 2 add, 3 quit): 1 #
# name: peter                          #
# 040-5466745                          #
# command (1 search, 2 add, 3 quit): 1 #
# name: mary                           #
# no number                            #
# command (1 search, 2 add, 3 quit): 2 #
# name: peter                          #
# number: 09-22223333                  #
# ok!                                  #
# command (1 search, 2 add, 3 quit): 1 #
# name: peter                          #
# 040-5466745                          #
# 09-22223333                          #
# command (1 search, 2 add, 3 quit): 3 #
# quitting...                          #
#--------------------------------------#


## My solution:
def phone_book():
    phone_book = {} # phone_book[name] = [number] (name is key, value here is a list of numbers)
    # phone_book stores lists of phone numbers: {"name": ["num1", "num2", etc]}
    while True:
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == "3":
            print("quitting...")
            break
        if command == "2":
            name = input("name: ")
            number = input("number: ")
            #add the number to the list of numbers for that name
            if name in phone_book:
                phone_book[name].append(number) #add this number to the list of numbers under that name
            else:
                phone_book[name] = [number] #if name doesnt exist yet, create a new list with this number as the only element. [] indicates the value is a LIST
            print("ok!")
        if command == "1":
            name = input("name: ")
            if name in phone_book:
                for number in phone_book[name]:
                    print(number)
            else:
                print("no number")

phone_book()


## The model solution provided:
# def search(persons):
#     name = input("name: ")
#     if name in persons:
#         for number in persons[name]:
#             print(number)
#     else:
#         print("no number")
 
# def add(persons):
#     name = input("name: ")
#     number = input("number: ")
#     if name not in persons:
#         persons[name] = []
#     persons[name].append(number)
#     print("ok!")
 
# def main():
#     persons = {}
#     while True:
#         cmd = input("command (1 search, 2 add, 3 quit): ")
#         if cmd == "1":
#             search(persons)
#         if cmd == "2":
#             add(persons)
#         if cmd == "3":
#             break
#     print("quitting...")
 
# main()
