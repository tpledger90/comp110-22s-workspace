"""Step 3 of Making Wordle...User will now have 5 guesses at the secret word."""

__author__ = "730477982"
"""from pickle import TRUE"""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(main_str: str, search_str: str) -> bool:
    """Searches through main_str and returns true if the seach_str is found within the main_str."""
    assert len(search_str) == 1
    count: int = 0

    while count < len(main_str):
        """Loops through the entire main string."""
        if main_str[count] == search_str:
            return True

        count += 1
    
    return False


def emojified(scrt_wrd: str, usr_guess: str) -> str:
    """Given a user guess and the secret word, will return the string of emojis that correspond with their guess."""
    assert len(usr_guess) == len(scrt_wrd)

    count: int = 0
    emoji_str: str = ""

    while count < len(scrt_wrd):
        """Loops through entire secret word, checking at every index and assigning to a certain box."""
        if usr_guess[count] == scrt_wrd[count]:
            emoji_str += GREEN_BOX
        elif contains_char(scrt_wrd, usr_guess[count]):
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        count += 1
    
    return emoji_str


def input_guess(expected_len: int) -> str:
    """Given an expected length (length of the secret word), will prompt user to input a guess of correct length until one is given."""  
    correct_guess: bool = False
    usr_guess: str = input(f"Enter a {expected_len} character word: ")

    while not correct_guess:
        """Loops until user gives an appropriate guess."""
        if len(usr_guess) == expected_len:
            correct_guess = True
        else:
            usr_guess = input(f"That wasn't {expected_len} chars! Try again: ")
    
    return usr_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    scrt_wrd: str = "codes"
    game_won: bool = False
    game_round: int = 1

    while not game_won and game_round <= 6:
        """Loops while the game has not been won yet and when the game round is at 6 or lower (if either become false, it stops looping)."""
        print(f"=== Turn {game_round}/6 ===")
        usr_guess = input_guess(len(scrt_wrd))
        print(emojified(scrt_wrd, usr_guess))

        if(usr_guess == scrt_wrd):
            print(f"You won in {game_round}/6")
            game_won = True
        else:
            game_round += 1

        if game_round == 7:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
