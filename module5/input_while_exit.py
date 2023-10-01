"""
Program: input_while_exit.py
Author: Liam P Reardon
Last date modified: 09/27/2023
This program prompts the user for numeric input between 1 and 100, and continues to prompt the user until the input is in the correct range
Once a the input is correct, the input will be stored in a list.
Once the user inputs the sentinel value of -1, the program will print all the numbers in the list and quit
"""

# Declare an empty list to store the valid inputs
inputs = []

SENTINEL = -1

user_input = int(input("Please enter a number between 1 and 100 (-1 to quit): "))

while user_input != SENTINEL:
        while user_input not in range(1, 101):
            user_input = int(input("[ERROR: INVALID INPUT] Please enter a number between 1 and 100 (-1 to quit): "))
            if user_input == SENTINEL:
                break
        if user_input == SENTINEL:
            break
        inputs.append(user_input)
        user_input = int(input("[NUMBER ACCEPTED!] Please enter a number between 1 and 100 (-1 to quit): "))

for x in inputs:
    print(x, end=", ")

"""
INPUT:          OUTPUT:
1,2,3,4,-1          1,2,3,4,-1

-1                  Nothing, quits

1337                "[ERROR: INVALID INPUT] Please enter a number..."
"""