"""
Program: sort_and_search_array.py
Author: Liam P Reardon
Last date modified: 10/18/2023
Class: CIS-189
This program searches and sorts a hardcoded array, then prompts the user for an item to search for in the array and returns its index
"""

def search_array(array, item):
    """
    :returns the index of the item if found, otherwise returns -1
    """
    if item in array:
        return array.index(item)
    else:
        return -1

def sort_array(array):
    """
    :returns the sorted array
    """
    array.sort()
    # included return statement because we're only doing calculations here, then returning the output
    return array

def main():
    list = [78, 1337, 1776, 13, 21]
    # calls sort array function
    sorted_list = sort_array(list)

    print("Original list: " + str(list)
    print("Sorted list: " + str(sorted_list))

    item = int(input("Please enter an item to search for: "))
    index = search_array(sorted_list, item)

    if index == -1:
        print("ERROR: Item not found!")
    else:
        print("Item found at index: " + str(index))

if __name__ == '__main__':
    main()