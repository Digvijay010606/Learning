# calculates the expenses of the user and returns the monthly and yearly income and savings

import os


def income_calculator() -> None :

    os.system("clear")
    
    monthly_income: float = float(input("Ener your monthly income: "))
    tax_rate: float =  float(input("Enter the tax rate: "))
    currency: str = input("Enter the currency: ")

    yearly_income: float = monthly_income * 12

    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12

    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = monthly_net_income * 12

    print("-" * 40)
    print(f"Yearly income: {currency} {yearly_income}")
    print(f"Monthly tax: {currency} {monthly_tax}")
    print(f"Yearly tax: {currency} {yearly_tax}")
    print(f"Monthly in-hand income: {currency} {monthly_net_income}")
    print(f"Yearly in-hand income: {currency} {yearly_net_income}")
    print("-" * 40)
     




if __name__ == "__main__":
    income_calculator()

