def calculate_ratios(income, expenses, debt, savings):
    debt_to_income = debt / income
    expense_ratio = expenses / income
    savings_ratio = savings / income

    return {
        "debt_to_income": round(debt_to_income, 2),
        "expense_ratio": round(expense_ratio, 2),
        "savings_ratio": round(savings_ratio, 2)
    }
