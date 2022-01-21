"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730477982"

usr_word: str = input("Enter a 5-character word: ")
if len(usr_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
usr_char: str = input("Enter a single character: ")
if len(usr_char) != 1:
        print("Error: Character must be a single character")
        exit()
count: int = 0

print("Searching for " + usr_char + " in " + usr_word)

if usr_word[0] == usr_char:
    print(usr_char + " found at index 0")
    count += 1
if usr_word[1] == usr_char:
    print(usr_char + " found at index 1")
    count += 1
if usr_word[2] == usr_char:
    print(usr_char + " found at index 2")
    count += 1
if usr_word[3] == usr_char:
    print(usr_char + " found at index 3")
    count += 1
if usr_word[4] == usr_char:
    print(usr_char + " found at index 4")
    count += 1

if count == 0:
    print("No instances of " + usr_char + " found in " + usr_word)
if count == 1:
    print("1 instance of " + usr_char + " in " + usr_word)
if count == 2:
    print("2 instances of " + usr_char + " in " + usr_word)




