# Loan Payment Calculator

def calculate_monthly_payment(principal, annual_interest_rate, years):
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate the number of monthly payments
    months = years * 12

    # Calculate the monthly payment
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)

    return monthly_payment

def main():
    print("Welcome to the Loan Payment Calculator")
    print("--------------------------------------")

    principal = float(input("Enter the loan amount: $"))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the number of years: "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)

    print("\nYour monthly payment will be: $", round(monthly_payment, 2))

if __name__ == "__main__":
    main()
