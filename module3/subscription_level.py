"""
Program: subscription_level.py
Author: Liam P Reardon
Last date modified: 09/13/2023
The purpose of this program is to ask a user what membership level they want, and then print the cost
The input is a number chosen by the user that corresponds to a membership tier
The output is the cost of that membership tier
"""

# Prints welcome message and displays membership options
print("Thank you for signing up for the Programmer's Toolkit Monthly Subscription Box!")
print("1) Platinum\n2) Gold\n3) Silver\n4) Bronze\n5) Free Trial")

# Grabs user input in the form of a number
chosen_level = input("Please enter a number that corresponds with an available membership level above: ")

# Calculates the correct output based on the chosen level
if chosen_level == "1":
    price = 60
    subscription = "Platinum"
elif chosen_level == "2":
    price = 50
    subscription = "Gold"
elif chosen_level == "3":
    price = 40
    subscription = "Silver"
elif chosen_level == "4":
    price = 30
    subscription = "Bronze"
elif chosen_level == "5":
    price = 0
    subscription = "Free Trial"
else:
    print("Please choose a number 1-5 that corresponds to a subscription level above")
    quit()

print(f"{subscription} subscription costs: ${price}")

#INPUT   EXPECTED OUTPUT                       ACTUAL OUTPUT
#hello   "Please enter a number 1-5..."        "Please enter a number 1-5..."
# 5       Free Trial subscription costs: $30   Free Trial subscription costs: $30  
# 1       Platinum subscription costs: $60     Platinum subscription costs: $60