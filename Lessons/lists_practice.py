"""Basic syntax of lists."""

# creating empty lists
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # Constructor


# adding a value to a list
my_numbers.append(1.5)

# String analogy
my_name: str = ""  # literal
my_name: str = str()  # constructor

# Creating an already populated list
game_points: list[str] = ["jump", "sing", "bananas"]
game_points.append("bananas")

# Modifying by index
game_points[1] = 72

# Indexing and or subscription notation
# Because lists are mutable

last_game: int = game_points[2]


# doesn't work with strings because they're immutable
# class_num: str = "110"  # change it to 210
# class_num[0] = "2"

# Getting the length of a list
(len(game_points))

# removing an item
game_points.pop(1)
print(game_points)


def display(int_list: list[int]) -> None:
    """ "Displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
