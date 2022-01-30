"""One-Shot Wordle: User will have one attempt at guessing the secret word and an accurate "wordle" response will be given using emojis."""

__author__ = "730477982"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_wrd: str = "python"
valid_guess: bool = False
usr_guess: str = input(f"What is your {len(secret_wrd)}-letter guess? ")

"""Loops until user inputs a guess of the correct length"""
while not valid_guess:
    if len(usr_guess) == len(secret_wrd):
        valid_guess = True
    else:
        usr_guess = input(f"That was not {len(secret_wrd)} letters! Try again: ")

count: int = 0
result_boxes: str = ""

"""Loops through the user's guess and assigns the correct corresponding boxes"""
while count < len(usr_guess):
    if usr_guess[count] == secret_wrd[count]:
        result_boxes += GREEN_BOX
    else:
        chr_exists_elswhr: bool = False
        count2: int = 0

        """Loop tests whether or not the current character of the user's guess is at any index of the secret word"""
        while (not chr_exists_elswhr) and (count2 < len(usr_guess)):
            if secret_wrd[count2] == usr_guess[count]:
                chr_exists_elswhr = True
            else:
                count2 += 1

        if chr_exists_elswhr:
            result_boxes += YELLOW_BOX
        else:
            result_boxes += WHITE_BOX
    count += 1

print(result_boxes)

if(usr_guess == secret_wrd):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")