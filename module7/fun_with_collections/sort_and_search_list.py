"""
Program: sort_and_search_list.py
Author: Liam P Reardon
Last date modified: 10/11/2023
Class: CIS-189
This program calls the make_list() function from basic_list.py to create a list of 4 numbers, then sorts the list and searches for a number in the list using sort_list() and search_list()
"""

# imports the basic_list.py file so we can use the make_list function
import basic_list

def sort_list():
    # included a return statement here since we're only manipulating the pre-created list and returning the sorted version for printing in main
    sorted_list = generated_list
    sorted_list.sort()
    return sorted_list

def search_list():
    # included a return statement since we're only calculating the index of the selected number and returning it for printing in main
    search = int(input("Please enter a number to search for in the list:"))
    if search in generated_list:
        return generated_list.index(search)
    else:
        return -1

if __name__ == '__main__':
    # generate the list for use in the sort and search functions
    generated_list = basic_list.make_list(4)
    # prints the sorted list
    print(sort_list(), "- Sorted List")
    # prints the index of the selected number in the list
    print("Index of selected number in list:", search_list())