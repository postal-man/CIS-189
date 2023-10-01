
"""
Program: coupon_calculations.py
Author: Liam P Reardon
Last date modified: 09/13/2023
This program accepts user input in the form of cost, cash off coupons, and a percent discount
This program then calculates this information and applies sales tax, then outputs the total
"""

# Sales tax rate constant
SALES_TAX = 0.06

# Initializes shipping cost variable for use below
shipping_cost = 0

# Sets user input to variables, very simple implementation with no input sanitization (I hope that's okay!)
cost = float(input("Please enter the amount of the purchase in USD: "))
cash_off = float(input("Please enter the cash-off coupon amount ($5 or $10): "))
percent_discount = float(input("Please enter the percent discount amount (10%, 15%, or 20%): "))

# Calculates cash-off coupon subtotal before percent discounts
cash_off_subtotal = cost - cash_off

# Calculates percent discount subtotal using cash off subtotal.  Divides percent discount by 100 to convert to decimal.
percent_discount_subtotal = cash_off_subtotal - (cash_off_subtotal * (percent_discount / 100))

# Calculates shipping fees using nested if statements, all values above 50 revert to shipping cost amount which is zero
if percent_discount_subtotal <= 10:
    shipping_cost = 5.95
elif percent_discount_subtotal <= 30:
    shipping_cost = 7.95
elif percent_discount_subtotal <= 50:
    shipping_cost = 11.95

# Calculates the total tax amount
total_tax = percent_discount_subtotal * SALES_TAX

# Calculates the final total by adding discounted subtotal, tax, and shipping cost
final_total = percent_discount_subtotal + total_tax + shipping_cost

# Returns calculated output to user
print(f"\nSubtotal: ${cost:.2f}")
print(f"Discounted Subtotal: ${percent_discount_subtotal:.2f}")
print(f"Sales Tax amount: ${total_tax:.2f}")
print(f"Total order amount: ${final_total:.2f}")