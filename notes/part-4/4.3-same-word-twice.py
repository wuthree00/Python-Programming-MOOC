## Please write a program which asks the user for words.
## If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

## Sample output:
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words


## Solution:
wordlist = []
word = input("Word: ")
wordlist.append(word)

while True:
    word = input("Word: ")
    if word in wordlist:
        wordlist.remove(word)
        print(f"You typed in {1+len(wordlist)} different words")
        break
    else:
        wordlist.append(word)
