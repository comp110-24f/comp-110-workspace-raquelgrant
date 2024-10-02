""""Challenge Question using a while loop"""  # docstring explaining code

__author__ = "730663103"  # stating my identity


def num_instances(phrase: str, search_char: str) -> int:  # defining fn.
    count: int = 0  # create local variable for number that counts instances of char
    index: int = 0  # create local variable for number of letters in phrase

    while index < len(
        phrase
    ):  # create loop when num of characters is less than in phrase
        char: str = phrase[index]  # create local variable for character in phrase
        if (
            search_char == char
        ):  # if stating when char. you're looking for is char. you found
            count = count + 1  # when above true add to counter
        index = index + 1  # reassign local var. inc. by one to move to next letter
    return count  # return back to count to loop again
