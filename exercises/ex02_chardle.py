""""EX02 - Chardle - A cute step toward Wordle."""  # docstring explaining code

__author__ = "730663103"


def input_word() -> str:  # defining fn. to get players guess word
    guess: str = input("Enter a 5-character word: ")  # local var. of player's word
    if len(guess) == 5:  # what to do if guess is right amt. of letters
        return guess
    else:  # what to do if guess is wrong amt. of letters
        print(str("Error: Word must contain 5 characters."))
        exit()


def input_letter() -> str:  # defining fn. to get players to choose word to check
    char: str = input("Enter a single character: ")  # local var of player's letter
    if len(char) == 1:  # what to do if right amt. of letters
        return char
    else:  # what to do if wrong amt. of letters
        print(str("Error: Character must be a single character."))
        exit()


def contains_char(
    guess: str, char: str
) -> None:  # defining fn. to check how often letter is in word
    print(
        str("Searching for " + str(char) + " in " + str(guess))
    )  # print what we're looking for
    counter: int = 0  # local var. for amount of instances in word
    if guess[0] == char:  # check if letters match at index 0
        print(str(char + " found at index 0"))
        counter += 1
    if guess[1] == char:  # check if letters match at index 1
        print(str(char + " found at index 1"))
        counter += 1
    if guess[2] == char:  # check if letters match at index 2
        print(str(char + " found at index 2"))
        counter += 1
    if guess[3] == char:  # check if letters match at index 3
        print(str(char + " found at index 3"))
        counter += 1
    if guess[4] == char:  # check if letters match at index 4
        print(str(char + " found at index 4"))
        counter += 1

    if counter == 0:  # what to print if no instances
        print("No instances of " + str(char) + " found in " + str(guess))
    elif counter == 1:  # what to print if 1 instance
        print("1 instance of " + str(char) + " found in " + str(guess))
    else:  # what to print for instances greater than 1
        print(str(counter) + " instances of " + str(char) + " found in " + str(guess))


def main() -> None:  # brings all together
    return contains_char(guess=input_word(), char=input_letter())


if __name__ == "__main__":  # calls main
    main()
