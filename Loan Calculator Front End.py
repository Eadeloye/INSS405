import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Loan Payment Calculator")

# Create labels
label_principal = tk.Label(root, text="Loan Amount ($)")
label_interest = tk.Label(root, text="Annual Interest Rate (%)")
label_years = tk.Label(root, text="Number of Years")

# Create entry fields
entry_principal = tk.Entry(root)
entry_interest = tk.Entry(root)
entry_years = tk.Entry(root)

# Create a result label
result_label = tk.Label(root, text="Monthly Payment: $")

# Create a calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)

def calculate():
    principal = float(entry_principal.get())
    annual_interest_rate = float(entry_interest.get())
    years = int(entry_years.get())

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)

    result_label.config(text=f"Monthly Payment: ${round(monthly_payment, 2)}")

label_principal.grid(row=0, column=0)
label_interest.grid(row=1, column=0)
label_years.grid(row=2, column=0)
entry_principal.grid(row=0, column=1)
entry_interest.grid(row=1, column=1)
entry_years.grid(row=2, column=1)
result_label.grid(row=3, column=0, columnspan=2)
calculate_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
