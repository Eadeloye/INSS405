# Collect five inputs from the user
numbers = []
for i in range(5):
    try:
        user_input = float(input(f"Enter number {i + 1}: "))
        numbers.append(user_input)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        break

# Calculate the sum of the numbers
total = sum(numbers)

# Calculate the average
if numbers:
    average = total / len(numbers)
else:
    average = 0  # Handle the case where no valid numbers were entered

# Print the sum and average
print(f"Sum of the numbers: {total:.2f}")
print(f"Average of the numbers: {average:.2f}")
