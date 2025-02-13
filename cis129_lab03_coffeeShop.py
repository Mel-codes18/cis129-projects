# Program: Text Based Coffee Shop Simulator
# Description: A simple interactive text-based coffee shop simulator
#              that calculates the receipt based on customer input
# Author: [M-dogg]
# Date: [2/12/25]

# Constants
COFFEE_PRICE = 5.00
LATTE_PRICE = 6.00
MUFFIN_PRICE = 4.00
PARFAIT_PRICE = 6.00
TAX_RATE = 0.06

# Input: Number of coffees and muffins the user is purchasing
num_coffees = int(input("Number of coffees bought? "))
num_lattes = int(input("Number of lattes bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_parfaits = int(input("Number of lattes bought? "))

# Calculate subtotal
subtotal_coffee = num_coffees * COFFEE_PRICE
subtotal_latte = num_lattes * LATTE_PRICE
subtotal_muffin = num_muffins * MUFFIN_PRICE
subtotal_parfait = num_parfaits *   PARFAIT_PRICE
subtotal = subtotal_coffee + subtotal_latte + subtotal_muffin + subtotal_parfait

# Calculate tax
tax = subtotal * TAX_RATE

# Calculate total
total = subtotal + tax

# Output: Display the receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print("***************************************")
print(f"{num_coffees} Coffee(s) at ${COFFEE_PRICE:.2f} each: ${subtotal_coffee:.2f}")
print(f"{num_lattes} Latte(S) at ${LATTE_PRICE:.2f} each: ${subtotal_latte:.2f}")
print(f"{num_muffins} Muffin(s) at ${MUFFIN_PRICE:.2f} each: ${subtotal_muffin:.2f}")
print(f"{num_parfaits} Parfait(s) at ${PARFAIT_PRICE:.2f} each ${subtotal_muffin:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
