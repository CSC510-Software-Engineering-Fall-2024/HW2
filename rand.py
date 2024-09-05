"""
This module contains a function to generate random numbers.
"""

import secrets


def random_array(arr):
    """
    Replace elements of arr with cryptographically secure random numbers.

    Args:
        arr (list): A list of integers to be replaced with random values.

    Returns:
        list: The modified list with random integers.
    """
    for i in range(len(arr)):
        # Generates a secure random number between 1 and 20
        arr[i] = secrets.randbelow(20) + 1
    return arr
