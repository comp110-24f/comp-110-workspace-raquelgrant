""""Mutating Functions."""  # docstring explaining code

__author__ = "730663103"  # stating my identity


def manual_append(group: list[int], num: int) -> None:  # defining fn. to add to list
    group.append(num)  # using append to add to


def double(nums: list[int]) -> None:  # defining fn. that will double list
    idx: int = 0  # setting index to 0 to allow to iterate through all items in list
    while idx < len(nums):  # setting loop for the length of list
        nums[idx] = nums[idx] * 2  # mutating all items in list to double
        idx += 1  # adding one to index to iterate to next item
    return  # return nothing


list_1: list[int] = [1, 2, 3]  # creating global var. for list 1
list_2: list[int] = list_1  # setting list 2 equal to list 1

double(list_2)  # applying double function to list 2
print(list_1)  # printing list 1
print(list_2)  # printing list 2
