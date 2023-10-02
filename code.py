import tkinter as tk
from PIL import Image, ImageTk  # Import the necessary modules for image handling
import random

# Initialize game variables
money = 1000
bank_level = 1
bank_capacity = 1000
bank_interest_rate = 0.05
population = 10

# Define Building class for custom building attributes
class Building:
    def __init__(self, name, cost, income_increase, capacity_increase, image_path):
        self.name = name
        self.cost = cost
        self.income_increase = income_increase
        self.capacity_increase = capacity_increase
        self.image = Image.open(image_path)  # Load custom building image
        self.image = self.image.resize((360, 360), Image.ANTIALIAS)  # Resize if needed
        self.image_tk = ImageTk.PhotoImage(self.image)  # Convert to Tkinter-compatible format

# Create instances of custom buildings with image paths
building1 = Building("Small House", 500, 50, 100, "building1.png")
building2 = Building("Apartment", 1000, 100, 250, "building2.png")

# Function to expand the bank
def expand_bank():
    global money, bank_level, bank_capacity
    cost = bank_level * 1000  # Cost to expand the bank
    if money >= cost:
        money -= cost
        bank_level += 1
        bank_capacity += 500
        update_display()
    else:
        status_label.config(text="Not enough money to expand!")

# Function to purchase and apply a building's effects
def purchase_building(building):
    global money, bank_capacity
    if money >= building.cost:
        money -= building.cost
        bank_capacity += building.capacity_increase
        income_increase = building.income_increase
        # Add the income increase to the next turn's income
        update_display()
        # Update the building's image to the purchased version
        building_label.config(image=building.image_tk)
    else:
        status_label.config(text=f"Not enough money to buy {building.name}!")

# Function to end the turn
def end_turn():
    global money, population
    population += 5
    income = bank_level * 100  # Income based on bank level
    money += income
    update_display()

# Function to update the display
def update_display():
    money_label.config(text=f"Money: ${money}")
    population_label.config(text=f"Population: {population}")
    bank_level_label.config(text=f"Bank Level: {bank_level}")
    bank_capacity_label.config(text=f"Bank Capacity: {bank_capacity}")
    bank_interest_label.config(text=f"Bank Interest Rate: {bank_interest_rate * 100}%")

# Create the main application window
root = tk.Tk()
root.title("Bank Tycoon Game")

# Create and pack widgets
money_label = tk.Label(root, text=f"Money: ${money}")
money_label.pack()
population_label = tk.Label(root, text=f"Population: {population}")
population_label.pack()
bank_level_label = tk.Label(root, text=f"Bank Level: {bank_level}")
bank_level_label.pack()
bank_capacity_label = tk.Label(root, text=f"Bank Capacity: {bank_capacity}")
bank_capacity_label.pack()
bank_interest_label = tk.Label(root, text=f"Bank Interest Rate: {bank_interest_rate * 100}%")
bank_interest_label.pack()

expand_button = tk.Button(root, text="Expand Bank", command=expand_bank)
expand_button.pack()
building1_button = tk.Button(root, text=f"Buy {building1.name}", command=lambda: purchase_building(building1))
building1_button.pack()
building2_button = tk.Button(root, text=f"Buy {building2.name}", command=lambda: purchase_building(building2))
building2_button.pack()
end_turn_button = tk.Button(root, text="End Turn", command=end_turn)
end_turn_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Create a label for displaying the building image
building_label = tk.Label(root, image=None)
building_label.pack()

# Start the main event loop
root.mainloop()


