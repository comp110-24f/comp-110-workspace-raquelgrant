"""Testing the lists made on other file. """

__author__ = "730663103"  # stating my identity

from exercises.ex05.utils import (
    only_evens,
    sub,
    add_at_index,
)  # importing funcs. from other file
import pytest  # importing the python test


def test_only_evens_basic_use() -> None:  # defining fn. to test basic use of only evens
    """Testing that only evens gives back a list with only even numbers"""
    assert only_evens([2, 3, 6, 7, 8]) == [
        2,
        6,
        8,
    ]  # asserting that an example list returns correctly w only evens


def test_only_evens_no_mutation() -> (
    None
):  # defining fn that checks the only evens does not mutate
    """Testing that only evens does not mutate the original list"""
    b: list[int] = [1, 4, 5, 8, 9]  # example list to use
    only_evens(b)  # calling only evens w example list
    assert b == [1, 4, 5, 8, 9]  # asserting that example list is the same


def test_only_evens_edge() -> (
    None
):  # defining fn. to test only edge with unconventional use
    """Testing what only evens does when given a strange case of inputs"""
    assert (
        only_evens([]) == []
    )  # asserting that only evens with empty list returns empty list


def test_sub_basic_use() -> None:  # defining fn. to test sub basic use
    """Testing that sub returns a new list with only numbers between the ranges"""
    assert sub([12, 18, 23, 13, 4, 87], 1, 4) == [
        18,
        23,
        13,
    ]  # asserting fn. w example list returns list w numbers in example ranges


def test_sub_no_mutation() -> None:  # defining fn. to ensure no mutation
    """Testing that sub does not mutate the original list"""
    b: list[int] = [2, 4, 7, 56, 24]  # example list to use
    sub(b, 2, 4)  # calling example list with example index ranges
    assert b == [2, 4, 7, 56, 24]  # asserting example list has not changed


def test_sub_edge() -> None:  # defining fn. to test unconventional use
    """Testing what sub does when given an empty list"""
    assert sub([], 1, 6) == []  # asserting using empty list returns empty list


def test_add_at_index_basic() -> (
    None
):  # defining fn. to test add at index basic use return
    """Testing that add at index returns nothing"""
    b: list[int] = [2, 4, 7, 25]  # example list to use
    assert (
        add_at_index(b, 2, 3) is None
    )  # ensuring after calling only fn., fn returns nothing


def test_add_at_index_mutation() -> (
    None
):  # defining fn. to test that add at index does mutate list
    """Testing that add at index mutates the original list"""
    a: list[int] = [14, 7, 4, 3, 8, 9]  # example list to use
    add_at_index(a, 3, 5)  # calling fn. with example list and integers for index
    assert a == [14, 7, 4, 3, 8, 3, 9]  # assert that original list has changed


def test_add_at_index_index_error() -> None:  # defining fn. to check error
    """Testing what add at index does when index to add number is out of range"""
    b: list[int] = [2, 5, 7]  # example list to use
    with pytest.raises(IndexError):  # raising py test error
        add_at_index(
            b, 4, 6
        )  # asserting that with these given inputs IndexError would come up
