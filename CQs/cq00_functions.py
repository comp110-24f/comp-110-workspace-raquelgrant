""""Challegne Question 1."""

__author__ = "730663103"


def mimic(message: str) -> str:
    """Repeating the word I choose."""
    return message


print(mimic(message="Joy and Happiness"))


def main() -> None:
    """Function to pull other Functions together"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
