# finance_calculator.py

income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual and projected savings
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Print results (no extra decimals unless needed)
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")

