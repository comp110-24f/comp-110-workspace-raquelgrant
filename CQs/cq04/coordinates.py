"""One More Part of the Importing CQ"""  # Docstring explaining

__author__ = "730663103"  # stating my identity


def get_coords(
    xs: str, ys: str
) -> None:  # defining fn. with parameters and return type
    x_index: int = 0  # creating local variable for index of xs
    x_coord: str  # local variable storing x coordinate
    y_coord: str  # local variable storing y coordinate
    while x_index < len(xs):  # conditional to make fn. iterate the correct amt.
        x_coord = xs[
            x_index
        ]  # make local variable whatever character is that index of xs
        y_index: int = 0  # creating local variable for index of ys that resets w loops
        while y_index < len(ys):  # conditional to make fn. iterate the correct amt.
            y_coord = ys[
                y_index
            ]  # make local variable whatever character is that index of ys
            print(
                "(" + x_coord + "," + y_coord + ")"
            )  # print concatenation of both coordinates
            y_index += 1  # increase y index by one for next loop
        x_index += 1  # increase x index by one for next loop
