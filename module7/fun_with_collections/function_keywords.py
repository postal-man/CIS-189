"""
Program: function_keywords.py
Author: Liam P Reardon
Last date modified: 10/11/2023
Class: CIS-189
This program declares a function average_scores() to return the average of a list of scores, and the first & last name and course of the student
"""

def average_scores(*args, **kwargs):
    # Get average of scores
    average = sum(args)/len(args)
    # Get first name, last name, and course
    first_name = kwargs.get("first_name")
    last_name = kwargs.get("last_name")
    course = kwargs.get("course")
    # Format and return result for printing in main
    return "Result: Name = %s %s Average = %.2f Course = %s" % (first_name, last_name, average, course)


if __name__ == '__main__':
    # calls average_scores() and outputs the result based upon the input below
    print(average_scores(100, 99, 98, 97, 96, 52, first_name="Liam", last_name="Reardon", course="NET 373"))
    print(average_scores(99, 100, 78, 97, 90, first_name="Elliot", last_name="Alderson", course="Pentesting 101"))
    print(average_scores(57, 89, 26, 94, 32, first_name="Quentin", last_name="Tarantino", course="Filmmaking 101"))