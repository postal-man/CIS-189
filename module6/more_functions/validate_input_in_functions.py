"""
Program: validate_input_in_functions.py
Author: Liam P Reardon
Last date modified: 10/01/2023
The purpose of this program is to take parameters test_name, test_score, invalid_message (validates the test_score), then return a string with test name and the resulting output
"""

def score_input(test_name, test_score = -1, invalid_message = "Invalid test score!"):
    """
    Args: 
        test_name, test_score, invalid_message
    Returns: 
        test_name (str) and score, invalid, or ValueError messages
    """
    try:
        score = int(test_score)
    except ValueError:
        return f"{test_name}: ValueError encountered!"

    if 0 <= score <= 100:
        return f"{test_name}: {test_score}"
    else:
        return f"{test_name}: {invalid_message}"

if __name__ == "__main__":
    display_string = score_input("Test 1", 70)
    print(display_string)

    display_string = score_input("Test 2", -21)
    print(display_string)

    display_string = score_input("Test 3", 128)
    print(display_string)

    display_string = score_input("Test 4", "hello")
    print(display_string)