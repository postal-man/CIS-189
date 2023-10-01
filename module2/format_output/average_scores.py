"""
Program: average_scores.py
Author: Liam P Reardon
Last date modified: 09/20/2023
The purpose of this program is to calculate the average of 3 scores
The input is a users first and last name, age, and 3 scores
The output is the same as above, however it returns the calculated average of the scores
"""

# Score constant
SCORE_COUNT = 3

try:
    last_name = input('Please enter your last name: ')
except:
    print('Error: Invalid Input')
    last_name = "Unknown"
try:
    first_name = input('Please enter your first name: ')
except:
    print('ERROR: Invalid input')
    first_name = "Unknown"
try:
    age = int(input('Please enter your age in years: '))
except:
    print('ERROR: Invalid input')
    age = 18
try:
    score1 = float(input('Enter your first score: '))
except:
    print('ERROR: Invalid input')
    score1 = 0.0
try:
    score2 = float(input('Enter your second score: '))
except:
    print('ERROR: Invalid input')
    score2 = 0.0
try:
    score3 = float(input('Enter your third score: '))
except :
    print('ERROR: Invalid input')
    score3 = 0.0

finally:

    # This line calculates the average of the 3 scores and assigns it to score_avg variable
    score_avg = (score1 + score2 + score3) / SCORE_COUNT

    # Finally, this line outputs all info with the calculated average (with .2f restricting output to 2 decimal places)
    print(f'{last_name}, {first_name} age: {age} average grade: {score_avg:.2f}')

"""
Test 1:
    Input: 70.6, 60.5, 75.2
    Expected output: 68.77
    Actual output: 68.77

Test 2:
    Input: 89, 76.5, 90.7
    Expected output: 85.40
    Actual output: 85.40

Test 3:
    Input: 67, 79, 67.9
    Expected Output 71.30
    Actual output: 71.30
"""