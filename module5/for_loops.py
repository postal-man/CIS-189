"""
Program: for_loops.py
Author: Liam P Reardon
Last date modified: 09/25/2023
The purpose of this program is to output numbers in a list using for loops, then output all odd numbers in between 99 to 33 in descending order
"""

numbers = [7.62, 5.56, 10.25, 9.29, 3.14]
i=1

for x in numbers:
    i+=1
    print(x)

for x in reversed(range(33, 100)):
    if (x % 2) != 0:
        print(x)