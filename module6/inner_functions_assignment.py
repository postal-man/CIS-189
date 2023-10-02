"""
Program: inner_functions_assignment.py
Author: Liam P Reardon
Last date modified: 10/02/2023
Class: CIS-189
This program accepts a list of measurements for a rectangle and returns a string with perimeter and area
"""

# Defines the measurements function
def measurements(measures):
    """
    Args:
        measures: a list of measurements (length, width)
    Returns:
         a string with perimeter and area
    """
    def area(a_list):
        if len(a_list) == 1:
            return a_list[0] * a_list[0]
        elif len(a_list) == 2:
            return a_list[0] * a_list[1]

    def perimeter(a_list):
        if len(a_list) == 1:
            return a_list[0] * 4
        elif len(a_list) == 2:
            return (a_list[0] * 2) + (a_list[1] * 2)

    # Calculates permimeter and area and returns a string with the values
    return "Perimeter = " + str(perimeter(measures)) + " Area = " + str(area(measures))

# Main call
if __name__ == "__main__":
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)