"""
Program: basic_list.py
Author: Liam P Reardon
Last date modified: 10/10/2023
Class: CIS-189
This program declare two functions: make_list() to return a list of user input while, and get_input() to get one input and return it
"""

def get_input():
    # Get input from user
    user_input = input("Please enter a number: ")
    return user_input

def make_list(num):
    # Make a list of user input
    num_list = []
    try:
        for x in range(num):
            user_input = get_input()
            user_input = int(user_input)
            num_list.append(user_input)
    except ValueError:
        print("Please enter a numeric value")
    
    return num_list

if __name__ == '__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))
