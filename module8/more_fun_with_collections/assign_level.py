"""
Program: assign_level.py
Author: Liam P Reardon
Last date modified: 10/18/2023
Class: CIS-189
This program prompts the user for a level, and returns the points needed for that level
"""

def switch_level(selection):
"""
:param selection: User inputted level
:return: Points needed for level
"""
    level = {
        "N": 50,
        "B": 150,
        "E": 300,
        "A": 500
    }

    return level.get(selection)

def switch_level_name(selection):
"""
:param selection: User inputted level
:return: Name of level
"""

    level = {
        "N": "Novice",
        "B": "Beginner",
        "E": "Experienced",
        "A": "Advanced"
    }

    return level.get(selection)

def main():
"""
:return: User inputted level and points needed for level
"""
    selection = input("Please enter a level (N, B, E, A): ")
    level = switch_level(selection)
    level_name = switch_level_name(selection)

    print("Level: " + level_name + "\nPoints needed: " + str(level))

if __name__ == '__main__':
    main() 