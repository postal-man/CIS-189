"""
Program: set_membership.py
Author: Liam P Reardon
Last date modified: 10/16/2023
Class: CIS-189
This program declare a function: in_set() to check if a value is in a set, then calls it in main to test it
"""

def in_set(selected_set, value):
    """ 
    Check if value is in set
    :param selected_set: the set to check
    :param value: the value to check for
    :returns: True if value is in set, False if not
    """
    if value in selected_set:
        return True
    else:
        return False

def main():
    # Test if value is in set
    test_set = {"banana","apple","cherry"}
    test_value = "apple"
    test_value2 = "5"

    if in_set(test_set, test_value):
        print(f"The value '{test_value}' is in the set {test_set}")
    else:
        print(f"The value '{test_value}' is not in the set {test_set}")

    if in_set(test_set, test_value2):
        print(f"The value '{test_value2}' is in the set {test_set}")
    else:
        print(f"The value '{test_value2}' is not in the set {test_set}")

if __name__ == "__main__":
    main()
