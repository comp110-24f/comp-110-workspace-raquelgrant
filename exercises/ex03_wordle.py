""""EX03 - Coding my own wordle!"""  # docstring explaining code

__author__ = "730663103"


def input_guess(secret_word_len: int) -> str:  # defining fn. to get players guess word
    while True:
        guess = input(f"Enter a {secret_word_len}-character word: ")
        word_len: int = len(guess)
        if word_len == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: ")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Function that will look through secret word for specific characters."""
    assert len(char_guess) == 1
    letter_counter: int = 0

    while letter_counter < len(secret_word):
        if secret_word[letter_counter] == char_guess:
            return True
        letter_counter += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Function to change guessed letters into diff emojis based on accuracy"""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    char_counter: int = 0
    response: str = ""

    while char_counter < len(guess):
        if guess[char_counter] == secret[char_counter]:
            response += GREEN_BOX
        elif contains_char(secret, guess[char_counter]):
            response += YELLOW_BOX
        else:
            response += WHITE_BOX
        char_counter += 1
    return response


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 0

    while turns < 6:
        print(f" === Turn {turns + 1}/6 ===")

        guess = input_guess(len(secret))
        response = emojified(guess, secret)
        print(response)

        if guess == secret:
            print(f"You won in {turns + 1}/6 turns!")
            exit()

        turns += 1

    if turns == 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
