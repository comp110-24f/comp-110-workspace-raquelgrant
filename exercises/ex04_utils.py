""""EX04 - Practice with List Utility Functions!"""  # docstring explaining code

__author__ = "730663103"  # who i am


def all(
    int_list: list[int], num: int
) -> bool:  # defining. fn to check if all numbers equal int
    if len(int_list) == 0:
        return False
    for elem in int_list:  # using for in to iterate through list
        if elem != num:  # when any part of list is not equal to int
            return False  # say False
    return True  # if all parts of list equal int say true


def max(input: list[int]) -> int:  # defining fn that takes in a list of ints
    if len(input) == 0:  # setting what to do if the list is empty
        raise ValueError("max() arg is an empty List")
    biggest_value = input[
        0
    ]  # make var. for the biggest value as the first value in list

    for elem in input[1:]:  # checking next value in list
        if elem > biggest_value:  # if its bigger than first value
            biggest_value = elem  # make next value new biggest value

    return biggest_value  # after iterating through all send back biggest


def is_equal(
    list_1: list[int], list_2: list[int]
) -> bool:  # defining fn. that takes two lists
    index: int = 0  # setting index at 0
    if len(list_1) != len(list_2):  # check if the lengths of the two list are equal
        return False  # if not stop there

    for index in range(
        len(list_1)
    ):  # checking index within the range of the first list
        if (
            list_1[index] != list_2[index]
        ):  # if int is diff. at the same index of the lists
            return False  # say false
    return True  # if all indexs for the list are equal say true


def extend(a: list[int], b: list[int]) -> None:  # defining fn. that takes two lists
    index: int = 0  # setting index as 0
    while index < len(b):  # check if index is less than length of 2nd list
        a.append(b[index])  # using append to add 2nd list at that index to 1st list
        index += 1  # adding to index
