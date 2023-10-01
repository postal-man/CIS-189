"""
Program: cast_to_integer.py
Author: Liam Reardon
Last date modified: 08/30/2023
The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

# Takes user input and assigns it to a user_input variable
user_input = input("Please enter input to be converted to an integer: ")

# Number variable takes user_input and modifies it by passing it through the float and int functions to account for numbers with decimals, then converts values to ints
number = int(float(user_input))

# Finally, print the modified number variable
print(number)

# Input   Expected Output  Actual Output
#    9             9               9
#   25.32         25             25
#   1215.2132    1215           1215
#  'hello'         ?                       Errors out: could not convert string to float