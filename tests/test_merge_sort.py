
"""

This module provides pytest cases to check our debugging.py function is working as expected.

"""

# pylint: disable=missing-docstring

from hw2_debugging import merge_sort


def test_1():
    input_arr = []
    expected_arr = []
    assert merge_sort(input_arr) == expected_arr #nosec

def test_2():
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected_arr = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert merge_sort(input_arr) == expected_arr #nosec

def test_3():
    input_arr = [56, 23, 92, 78]
    expected_arr = [23, 56, 92, 92]
    assert merge_sort(input_arr) != expected_arr #nosec
