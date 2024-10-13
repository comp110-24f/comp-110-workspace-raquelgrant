"""Summing the elements of a list using different loops."""

__author__: str = "730663103"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    total: float = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


print(w_sum([1.1, 0.9, 1.0]))


def f_sum(vals: list[float]) -> float:
    total = 0
    for num in vals:
        total += num
    return total


print(f_sum([1.1, 0.9, 1.0]))


def f_range_sum(vals: list[float]) -> float:
    total = 0
    for index in range(len(vals)):
        total += vals[index]
    return total


print(f_range_sum([1.1, 0.9, 1.0]))
