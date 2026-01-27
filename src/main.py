from data_processing import calculate_ratios
from risk_model import train_risk_model, predict_risk
from recommendation_engine import generate_recommendations

print("\nAI-Driven Personal Finance Advisor System\n")

income = float(input("Enter monthly income (₹): "))
expenses = float(input("Enter monthly expenses (₹): "))
debt = float(input("Enter total debt (₹): "))
savings = float(input("Enter current savings (₹): "))

ratios = calculate_ratios(income, expenses, debt, savings)

model = train_risk_model()
risk_level = predict_risk(model, income, expenses, debt, savings)

recommendations = generate_recommendations(risk_level, ratios)

print("\n--- Financial Analysis Report ---")
print(f"Debt-to-Income Ratio : {ratios['debt_to_income']}")
print(f"Expense Ratio        : {ratios['expense_ratio']}")
print(f"Savings Ratio        : {ratios['savings_ratio']}")
print(f"Overall Risk Level   : {risk_level}")

print("\n--- Personalized Recommendations ---")
for rec in recommendations:
    print(f"- {rec}")
