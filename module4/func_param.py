"""
Program: func_param.py
Author: Liam P Reardon
Last date modified: 09/20/2023
This program accepts a string to be repeated, and an integer that determines how many times to repeat it
The output is the string repeated
"""

def multiply_string(message: str, n: int):
    try:
        if n < 1:
            raise Exception
    except:
        return 'ERROR: Number must be greater than or equal to 1'
    else:
        return message * n

if __name__ == '__main__':
    print(multiply_string('Python!', 0.55))