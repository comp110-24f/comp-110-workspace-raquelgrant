""" Max func. test for CQ7. """  # describing docstring

__author__ = "730663103"  # who i am

from CQs.cq07.find_max import find_and_remove_max  # importing func. from other file


def test_find_max_basic_use() -> (
    None
):  # defining fn. to test that the fn. returns the biggest val.
    """Testing that find and remove funct. returns expected value"""  # docstring
    assert (
        find_and_remove_max([4, 5, 6, 7]) == 7
    )  # asserting that a use of the fn. gives back the right thing


def test_find_max_mutation() -> None:  # defining fn. to test that fn. mutates list
    """Testing that find and remove func. mutates list correctly"""  # docstring
    b: list[int] = [6, 8, 4, 8, 5]  # inputting an arbitrary list to use in test
    find_and_remove_max(b)  # running fn. using arbitraty list
    assert b == [6, 4, 5]  # checking that fn. removed all instances of biggest value


def test_find_max_edge() -> (
    None
):  # defining fn. to test if fn. works with unconvetional usage
    """Testing find and remove funct. on empty list"""  # docstring
    assert find_and_remove_max([]) == -1  # assert that empty list returns -1
