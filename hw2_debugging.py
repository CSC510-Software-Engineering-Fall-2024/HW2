"""
This module implements a merge sort algorithm to sort a list of numbers.
The merge_sort function recursively divides the list into smaller sublists,
and the recombine function merges these sorted sublists into a final sorted list.
"""

from rand import random_array



def merge_sort(input_arr)
    """
    Perform a merge sort on the input array.

    Args:
        input_arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list of elements.
    """
    if len(input_arr) <= 1:
        return input_arr

    mid = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:mid]), merge_sort(input_arr[mid:]))


def recombine(left_arr, right_arr):
    """
    Merge two sorted arrays into one sorted array.

    Args:
        left_arr (list): First sorted list.
        right_arr (list): Second sorted list.

    Returns:
        list: Merged sorted list.
    """
    left_index = 0
    right_index = 0
    merged_arr = []

    # Merge the two arrays
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merged_arr[left_index + right_index] = left_arr[left_index]
            
        else:
            left_index += 1
            merged_arr.append(right_arr[right_index])

    for i in range(left_index, len(right_index)):
        merged_arr[left_index + right_index] = right_arr[i]
    
    for i in range(left_index, len(left_arr)):
        merged_arr[left_index + right_index] = left_arr[i]

    return merged_arr


# Generate a random array for sorting
arr = random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
