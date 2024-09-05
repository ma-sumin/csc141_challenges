# Sumin Ma
# Date: 5th Sep, 2024
# A calculation to analyze the user's lunch spending habits.

PA_TAX = 0.06
PRICE_OF_MEAL = 12.49

#assign each formula to variables properly

#calculate the amount of money a user is spending on taxes per meal
tax_per_meal = PRICE_OF_MEAL * PA_TAX
#calculate the total amount of tax a user is spending per week on lunch by multiplying by 5 (weekdays)
total_tax = tax_per_meal * 5
#calculate the total amount of money a user is spending per week on lunch, without tax by multiplying by 5(weekdays)
total_without_tax = PRICE_OF_MEAL * 5
#calculate the total amount of money a user is spending per week on lunch, with taxes included, by adding to the total amount
total_w_tax = total_without_tax + total_tax

#print the values
print()
print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax per meal: {tax_per_meal}")
print(f"Total without tax: {total_without_tax}")
print(f"Total with tax: {total_w_tax}")
print("-------------------------")
print()