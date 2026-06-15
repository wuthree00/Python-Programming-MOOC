## Please write a program which asks the user to type in some text.
## Your program should then perform a spell check, and print out feedback to the user,
## so that all misspelled words have stars around them. Please see the two examples below:

# Sample output:
#-----------------------------------------------------#
# Write text: We use ptython to make a spell checker
# We use *ptython* to make a spell checker
#-----------------------------------------------------#

# Sample output:
#--------------------------------------------------------#
# Write text: This is acually a good and usefull program
# This is *acually* good and *usefull* program
#--------------------------------------------------------#

# The case of the letters should be irrelevant to the functioning of your program.

# The exercise template includes the file wordlist.txt,
# which contains all the words the spell checker should accept as correct.

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.

# NB2 If Visual Studio can't find the file and you have checked that there are no spelling errors,
# take a look at these instructions. (https://programming-26.mooc.fi/part-6/1-reading-files#what-if-visual-studio-code-cannot-find-my-file)


## My solution:
the_input = input("Write text: ") #the input as a string
the_words = the_input.split() #the input as a list of words
new_list_to_print = []

the_wordlist = []
# read the contents of the file and store it in a list
with open("wordlist.txt") as new_file:
    for line in new_file:
        the_wordlist.append(line.strip())

for word in the_words:
    if word.lower() in the_wordlist:
        new_list_to_print.append(word)
    else:
        new_list_to_print.append("*"+word+"*")

sentence = " ".join(new_list_to_print)
print(sentence)


## The model solution provided:
def wordlist():
    words = []
 
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
 
    return words
 
words = wordlist()
sentence = input("Write text: ")
 
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
 
print()
