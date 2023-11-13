"""Summing the elements of a list using different loops."""

__author__ = "730387751"


def w_sum(vals: list[float]) -> float:
    """Write a function that sums a list of floats with a while loop."""
    idx = 0
    sum = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Write a function that sums a list of floats with a for loop."""
    sum = 0.0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Write a function that sums a list of floats with a for loop and range."""
    sum = 0.0
    for idx in range(len(vals)):
        sum += vals[idx]
    return sum


vals: list[float] = [1.0, 5.5, 3.5]

print(w_sum(vals))
print(f_sum(vals))
print(f_range_sum(vals))
print(w_sum([]))
