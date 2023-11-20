for i in range(11):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using math.pi
area1 = math.pi * radius ** 2

# Print the result
print(area1)

import math

import math

# Calculate the area of the circle
radius = float(input("Enter the radius of the circle: "))
area_circle = math.pi * radius ** 2
print(f"Area of the circle: {area_circle}")

# Calculate the area of the rectangle
length_rectangle = float(input("Enter the length of the rectangle: "))
width_rectangle = float(input("Enter the width of the rectangle: "))
area_rectangle = length_rectangle * width_rectangle
print(f"Area of the rectangle: {area_rectangle}")

# Function to check and calculate the area
def area_check(Width, Length):
    # Check if inputs are greater than 0
    if Width > 0 and Length > 0:
        area = Width * Length
        return area
    else:
        print("Input parameters should be greater than 0. Cannot compute the area of the requested polygon.")
        return None

# Example usage of the function
result = area_check(width_rectangle, length_rectangle)
if result is not None:
    print(f"Area using the function: {result}")
