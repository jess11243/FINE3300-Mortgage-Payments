""""
Assignment 1: Mortgage Payments
Course: FINE3300 
Name: Jessica L. Draper
Date: 02/02/25

Purpose: Calculate mortgage payments for different payment frequencies

"""

# Determine what parameters to take for our function
def mortgage_payments(principal, rate, amortization):
    
    # Convert the user-inputted rate to a decimal
    rate = rate / 100
    
    # Our Present Value of Annuity function, implementing the PVA formula
    def pva(r, n):
        return (1 - (1 + r) ** -n) / r
    
    # Calculate rates (converting from semi-annual compound rate)
    # eg. monthly = (1 + rq/2)^(2/12) - 1, semi = (1 + rq/2)^(2/24) - 1 etc.
    monthly_rate = (1 + rate / 2) ** (2 / 12) - 1
    semi_monthly_rate = (1 + rate / 2) ** (2 / 24) - 1
    bi_weekly_rate = (1 + rate / 2) ** (2 / 26) - 1 # 52 / 2 = 26
    weekly_rate = (1 + rate / 2) ** (2 / 52) - 1 # 52 weeks in a year
    
    # Calculate number of payments for each frequency over the user-inputted amortization period
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52
    
    # Calculate the payment amounts by dividing the principal by the PVA factor
    # So that the payments can exactly pay off the loan over the specified amortization period
    monthly = principal / pva(monthly_rate, n_monthly)
    semi_monthly = principal / pva(semi_monthly_rate, n_semi_monthly)
    bi_weekly = principal / pva(bi_weekly_rate, n_bi_weekly)
    weekly = principal / pva(weekly_rate, n_weekly)
    
    # Accelerated payments, to calculate a faster loan repayment
    rapid_bi_weekly = monthly / 2
    rapid_weekly = monthly / 4
    
    return (monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly) # The 6-index tuple we will call

def main():
    # User input
    principal = float(input("Enter the principal amount: $")) # Used float b/c can be a decimal
    rate = float(input("Enter the annual interest rate (as a percentage, ex. 5.5, 6.89): ")) # Used float b/c can be a decimal
    amortization = int(input("Enter the amortization period (in WHOLE years, ex. 5, 7): ")) # Used int b/c assuming user will input whole years (no decimal)
    
    # Payment calculation
    payments = mortgage_payments(principal, rate, amortization)
    
    # Format and display results
    print(f"\nMortgage Payment Schedule:")
    print(f"Monthly Payment: ${payments[0]:.2f}") # Using .2f to round all the answers to 2 decimal places
    print(f"Semi-monthly Payment: ${payments[1]:.2f}") # Using a tuple (payments), acessing from there
    print(f"Bi-weekly Payment: ${payments[2]:.2f}") # Using the curly brackets to indicate a variable value
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")

"""""
Extra indexing for reference:

payments[0]   Monthly payment
payments[1]   Semi-monthly payment
payments[2]   Bi-weekly payment
payments[3]   Weekly payment
payments[4]   Rapid bi-weekly payment
payments[5]   Rapid weekly payment

"""

# Will only run if the file is not imported
if __name__ == "__main__":
    main()