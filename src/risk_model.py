import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_risk_model():
    data = pd.read_csv("data/user_financial_data.csv")

    X = data[['income', 'expenses', 'debt', 'savings']]
    y = data['risk_label']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    return model

def predict_risk(model, income, expenses, debt, savings):
    input_data = pd.DataFrame(
        [[income, expenses, debt, savings]],
        columns=['income', 'expenses', 'debt', 'savings']
    )

    prediction = model.predict(input_data)[0]
    labels = {0: "LOW RISK", 1: "MEDIUM RISK", 2: "HIGH RISK"}
    return labels[prediction]
