import math

# Investments
selling_price = 695985.00
bond_interest_rate = 10.85/100
deposit_percentage = 0
monthly_effective_interest_rate = bond_interest_rate / 12
bond_term = 30  # years
number_of_repayments = bond_term * 12

# Income
rental_income = 6000


# Expenses
levies = 1000
insurance = 300
incase_money = 500
property_management = rental_income * 10 / 100


# Upfront Invest Amount
down_payment = selling_price * deposit_percentage/100
asked_from_bank = selling_price - down_payment
security_gates = 7000
renovations = 2000  # Bathroom mirrors + soap dish
number_of_months_without_tenant = 4
occupation_interest = selling_price * (10/100) * number_of_months_without_tenant  # Before securing a tenant
electricity_water_meter_setup = 1500


# Analysis
monthly_repayments = asked_from_bank * (monthly_effective_interest_rate * math.pow(1 + monthly_effective_interest_rate, number_of_repayments)) / (math.pow(1 + monthly_effective_interest_rate, number_of_repayments) - 1)

monthly_cashflow_before_tax = rental_income - monthly_repayments - levies - insurance - property_management - incase_money

total_investment = down_payment + security_gates + renovations + occupation_interest + electricity_water_meter_setup

annual_cashflow = monthly_cashflow_before_tax * 12

return_on_investment = annual_cashflow / total_investment  # annual interest

print(f"monthly bond repayments = {monthly_repayments}")
print(f"annual return on investment (%) = {return_on_investment}")
