#Author: Michele Mora
#CIS-129
#4/29/25
#Module 10 Lab

#This code asks the user for a dollar amount and gives
#an amount with asterisks in the far left to produce 
#a dollar amount that is safer from fraudulent activity.

# Asks user for dollar amount
amount = input("Enter the dollar amount: ")

# Convert amount to string and strip leading/trailing white space
amount = str(amount).strip()

# Indicates numbers of asterisks depending on the amount
num_asterisks = 12 - len(amount)

# Applies the asterisks. 
asterisks = '*' * num_asterisks

# Uses Asterics and Amounts to make one variable
safe_amount = asterisks + amount

# Print the check-protected amount
print(safe_amount)