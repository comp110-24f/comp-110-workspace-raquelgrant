"""More work with Lists for EX05. """

__author__ = "730663103"  # stating my identity


def only_evens(
    numbers: list[int],
) -> list[int]:  # defining fn that will return only evens
    evens: list[int] = []  # create empty list that would be added to if number was even
    for elem in numbers:  # iterate through numbers
        if elem % 2 == 0:  # if remainder is zero(number is even)
            evens.append(elem)  # add number to evens list

    return evens  # return evens list


def sub(
    a_list: list[int], range1: int, range2: int
) -> list[int]:  # defining fn. to get numbers in between range
    new_list: list[int] = (
        []
    )  # create empty list that would be added to if number was in index range
    index: int = 0  # setting index counter to 0
    for elem in a_list:  # iterate through a list
        if (
            index >= range1 and index < range2
        ):  # ensure index is in between two given ranges
            new_list.append(elem)  # add number to new list
        index += 1  # add to index
    return new_list  # return new list


def add_at_index(
    list_1: list[int], int_added: int, index_added: int
) -> None:  # defining fn. to add a number to list at index
    if index_added < 0 or index_added > len(
        list_1
    ):  # if index to add is less than zero or longer than list
        raise IndexError("Index is out bounds for the input list")  # raise error
    list_1.append(0)  # add empty number to list to make space for new number
    index = len(list_1) - 2  # make index 2 less than length because non inclusive
    while index >= index_added:  # when index is more than that of the added number
        list_1[index + 1] = list_1[index]  # move indices up one
        index -= 1  # subtract from index
    list_1[index_added] = int_added  # add in new number at location of index added
