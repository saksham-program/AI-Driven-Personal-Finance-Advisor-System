def generate_recommendations(risk_level, ratios):
    recommendations = []

    if risk_level == "HIGH RISK":
        recommendations.append("Reduce unnecessary expenses immediately.")
        recommendations.append("Focus on paying off high-interest debt.")
        recommendations.append("Avoid taking new loans.")

    elif risk_level == "MEDIUM RISK":
        recommendations.append("Track monthly spending carefully.")
        recommendations.append("Increase savings where possible.")
        recommendations.append("Limit discretionary expenses.")

    else:
        recommendations.append("Your finances are stable. Continue saving.")
        recommendations.append("Consider long-term investments.")
        recommendations.append("Maintain disciplined spending habits.")

    if ratios["expense_ratio"] > 0.6:
        recommendations.append("Your spending is high compared to income.")

    if ratios["savings_ratio"] < 0.2:
        recommendations.append("Try to increase your monthly savings.")

    return recommendations
