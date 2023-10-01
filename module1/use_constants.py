"""
Program: use_constants.py
Author: Liam P Reardon
Last date modified: 08/29/2023
The purpose of this program is declare and print variables and constants
"""

import constants

# Sets quantity variable to int 13
quantity = 13
# Sets item variable to string shirts
item = "shirts"
# Sets size to a float of 6.0
size = 6.0

# Outputs all variables in the given format
print(quantity, item, "size", size)
# This print line outputs the item and concatenates "are $" with the price constant casted as a string
print(item, "are $", str(constants.PRICE))