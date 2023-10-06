Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

# Bank Tycoon - Basic Text-Based Version

# Initialize game variables
money = 1000  # Starting money
population = 10  # Starting population
bank_level = 1  # Bank's level
bank_capacity = 1000  # Initial bank capacity
bank_interest_rate = 0.05  # Initial interest rate

# Main game loop
while True:
    # Display player's resources
    print(f"Money: ${money}")
    print(f"Population: {population}")
    print(f"Bank Level: {bank_level}")
    print(f"Bank Capacity: {bank_capacity}")
    print(f"Bank Interest Rate: {bank_interest_rate * 100}%\n")

    # Menu options
    print("Options:")
    print("1. Expand Bank")
    print("2. Build Town")
    print("3. Offer Loan")
...     print("4. End Turn")
...     choice = input("Enter your choice: ")
... 
...     if choice == "1":
...         # Expand the bank
...         cost = bank_level * 200  # Cost increases with bank level
...         if money >= cost:
...             money -= cost
...             bank_level += 1
...             bank_capacity += 500  # Increase capacity on expansion
...         else:
...             print("Not enough money to expand the bank!")
... 
...     elif choice == "2":
...         # Build town buildings (simplified)
...         print("Building a town building... (simplified)")
... 
...     elif choice == "3":
...         # Offer a loan to a virtual citizen
...         loan_amount = int(input("Enter the loan amount: "))
...         if money >= loan_amount:
...             money -= loan_amount
...             interest_earned = loan_amount * bank_interest_rate
...             money += interest_earned
...             print(f"You earned ${interest_earned} in interest!")
... 
...     elif choice == "4":
...         # End turn (simplified population growth)
...         population += 5
...         money += bank_level * 100  # Income from the bank's operations
...         print("End of turn. Population increased and earned income.")
... 
...     else:
...         print("Invalid choice. Please select a valid option.")
... 
...     # Check for game over condition (simplified)
...     if money < 0:
...         print("Game over! You ran out of money.")
...         break
