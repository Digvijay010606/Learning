# calculates the expenses of the user and returns the monthly and yearly income and savings
from currency_formatting import format_currency
import os


def finance_calculator() -> None :

    os.system("clear")

    while True:
        try:
            monthly_income: float = float(input("Enter your monthly income: "))
            tax_rate: float = float(input("Enter the tax rate(%): "))
            currency: str = input("Enter the currency: ")
            print("Now add some basic expenses")
            rent: float = float(input("Enter your house rent: "))
            food: float = float(input("Enter your food cost: "))
            travel: float = float(input("Enter your travel cost: "))
            break

        except ValueError:
            print("Please! enter correct input")

    yearly_income: float = monthly_income * 12

    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12

    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = monthly_net_income * 12

    print("-" * 40)
    print("Income calculation".center(40))
    print(f"\nYearly income: {currency} {format_currency(yearly_income)}")
    print(f"Monthly tax: {currency} {format_currency(monthly_tax)}")
    print(f"Yearly tax: {currency} {format_currency(yearly_tax)}")
    print(f"Monthly in-hand income: {currency} {format_currency(monthly_net_income)}")
    print(f"Yearly in-hand income: {currency} {format_currency(yearly_net_income)}")
    print("-" * 40)
    
    print("Your expenses".center(40))
    print(f"\nHouse rent: {currency} {format_currency(rent)}")
    print(f"Food cost: {currency} {format_currency(food)}")
    print(f"Travel cost: {currency} {format_currency(travel)}\n")
    print("-"*40)
    print(f"Money left monthly: {format_currency(monthly_net_income - rent + food + travel)}")
    print(f"Money left yearly: {format_currency(yearly_net_income - ((rent + food + travel) * 12))}")
    print("-"*40)


if __name__ == "__main__":
    finance_calculator()

