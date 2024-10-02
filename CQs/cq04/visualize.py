"""Another Part of the Importing CQ"""  # Docstring explaining

__author__ = "730663103"  # stating my identity

from CQs.cq04.concatenation import concat  # importing concatenation file
from CQs.cq04.coordinates import get_coords  # importing coordinates file

x: str = "123"  # global variable to use
y: str = "abc"  # global variable to use

print(concat(x, y))  # calling concat fn.
get_coords(x, y)  # calling get_coords fn.
