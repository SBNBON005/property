import math

# Investments
selling_price = 695985.00
bond_interest_rate = 10.85/100
deposit_percentage = 0/100
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
down_payment = selling_price * deposit_percentage
asked_from_bank = selling_price - down_payment
security_gates = 7000
renovations = 2000  # Bathroom mirrors + soap dish
number_of_months_without_tenant = 5
occupation_interest = 1/100
occupation_rent = selling_price * occupation_interest * number_of_months_without_tenant  # Before securing a tenant
electricity_water_meter_setup = 1500
bond_initiation_fee = 6000


# Analysis
monthly_repayments = asked_from_bank * (monthly_effective_interest_rate * math.pow(1 + monthly_effective_interest_rate, number_of_repayments)) / (math.pow(1 + monthly_effective_interest_rate, number_of_repayments) - 1)

monthly_cashflow_before_tax = rental_income - monthly_repayments - levies - insurance - property_management - incase_money

total_investment = down_payment + security_gates + renovations + occupation_rent + electricity_water_meter_setup + bond_initiation_fee

annual_cashflow = monthly_cashflow_before_tax * 12

return_on_investment = annual_cashflow / total_investment  # annual interest

print(f"monthly bond repayments = {monthly_repayments}")
print(f"annual return on investment (%) = {return_on_investment}")
