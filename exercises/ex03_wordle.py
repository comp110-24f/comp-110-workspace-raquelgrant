""""EX03 - Coding my own wordle!"""  # docstring explaining code

__author__ = "730663103"  # who i am


def input_guess(secret_word_len: int) -> str:  # defining fn. to get players guess word
    while True:  # creating loop to make sure guess is length of secret word
        guess = input(
            f"Enter a {secret_word_len}-character word: "
        )  # creating var. for input guess
        word_len: int = len(guess)
        if word_len == secret_word_len:  # if length of guess is length of secret word
            return guess  # send guess to next part
        else:
            print(
                f"That wasn't {secret_word_len} chars! Try again: "
            )  # if wrong length loop back to original input question


def contains_char(
    secret_word: str, char_guess: str
) -> bool:  # defining fn. to check if specific character is in guessed word
    """Function that will look through secret word for specific characters."""
    assert len(char_guess) == 1  # ensure charact is only 1 letter
    letter_counter: int = 0  # setting index counter to zero

    while letter_counter < len(
        secret_word
    ):  # making loop for while index counter is less than length of secret word
        if (
            secret_word[letter_counter] == char_guess
        ):  # if letter at index counter matches specific char
            return True
        letter_counter += 1  # add to index counter to move to next letter in next loop

    return False  # if letter not found after looping through whole word


def emojified(
    guess: str, secret: str
) -> str:  # defining fn. to turn guesses into emojis
    """Function to change guessed letters into diff emojis based on accuracy"""
    assert len(guess) == len(
        secret
    )  # ensure length of guess and length of secret word are the same

    WHITE_BOX: str = (
        "\U00002B1C"  # local var. making name equivalent to code for white emoji
    )
    GREEN_BOX: str = (
        "\U0001F7E9"  # local var. making name equivalent to code for green emoji
    )
    YELLOW_BOX: str = (
        "\U0001F7E8"  # local var. making name equivalent to code for yellow emoji
    )
    char_counter: int = 0  # setting index counter for each letter of word
    response: str = ""  # preparing a str to put the response of emojis into

    while char_counter < len(
        guess
    ):  # creating loop that stops after last letter of guess
        if (
            guess[char_counter] == secret[char_counter]
        ):  # if letter is in word and in right index
            response += GREEN_BOX  # add emoji to response string
        elif contains_char(
            secret, guess[char_counter]
        ):  # calling contains char to check if letter is in word in wrong spot
            response += YELLOW_BOX  # add emoji to response string
        else:  # if letter is not in word at all
            response += WHITE_BOX  # add emoji to response string
        char_counter += 1  # add to index counter to move to next letter of guess
    return response  # send string of all emojis to next part


def main(secret: str) -> None:  # defining fn. to bring all fns. together
    """The entrypoint of the program and main game loop."""
    turns: int = 0  # create variable for whatever turn you're playing at

    while turns < 6:  # make loop for when turn is less than max amount of turns
        print(
            f" === Turn {turns + 1}/6 ==="
        )  # print message with specific amount of turns

        guess = input_guess(
            len(secret)
        )  # setting var. using input by calling input guess w len of secret
        response = emojified(
            guess, secret
        )  # setting var. response as emojis given by calling emojified
        print(response)  # printing emojis

        if guess == secret:  # if you did it correctly
            print(f"You won in {turns + 1}/6 turns!")  # print winner's statement
            exit()  # leave program

        turns += 1  # if you didn't get it, add to turns for next loop with next turn

    if turns == 6:  # if you hit max turns
        print("X/6 - Sorry, try again tomorrow!")  # print loser's statement


if __name__ == "__main__":
    main(secret="codes")  # calling main with codes as secret word
