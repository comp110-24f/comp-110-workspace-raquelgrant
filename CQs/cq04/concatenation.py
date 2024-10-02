"""One Part of the Importing CQ"""  # Docstring explaining

__author__ = "730663103"  # stating my identity


def concat(w1: str, w2: str) -> str:  # def fn. to put together parameters
    return w1 + w2  # returning concatenated version


word1: str = "happy"  # Global variable for calling
word2: str = "tuesday"  # Global variable for calling


if __name__ == "__main__":  # suppressing fn. call when imported
    print(concat(word1, word2))  # fn. call
