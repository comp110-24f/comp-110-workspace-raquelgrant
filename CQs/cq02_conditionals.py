""" Writing a simple number guessing game"""  # docstring title

__author__: str = "730663103"  # author PID


def guess_a_number() -> None:  # defining fn.
    secret: int = 7  # create local variable "secret"
    guess: str = input("Guess a number: ")  # write input question
    print("Your guess was " + str(guess))  # print statement saying what guess is

    if int(guess) == secret:  # stating what guess is if same as secret
        print("You got it!")  # printing correct message

    if int(guess) < secret:  # stating what guess is if less than secret
        print(
            "Your guess was too low! The secret number is " + str(secret)
        )  # printing "too low" message

    if int(guess) > secret:  # stating what guess is if more than secret
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # printing "too high" message


if __name__ == "__main__":  # establish main fn.
    guess_a_number()  # call guess fn.
