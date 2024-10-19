""" Max function for Challenge Question 7. """  # docstring describing whole thing

__author__ = "730663103"  # who i am


def find_and_remove_max(input: list[int]) -> int:  # fn. to find and remove biggest val.
    index: int = 0  # setting index as 0

    if len(input) == 0:  # what to do empty list
        return -1  # return this val.
        exit  # do not continue through fn.
    biggest_value = input[
        0
    ]  # make var. for the biggest value as the first value in list
    for elem in input:  # use for in to iterate through list
        if elem > biggest_value:  # when next item is bigger than previous biggest
            biggest_value = elem  # make current item new biggest value

    while index < len(input):  # create while loop for length of list
        if input[index] == biggest_value:  # if item in list is the biggest value
            input.pop(index)  # remove it from list
        else:  # ensuring index only changes when nothing was removed from list
            index += 1  # add to index to move to next item in list

    return biggest_value  # return biggest value
