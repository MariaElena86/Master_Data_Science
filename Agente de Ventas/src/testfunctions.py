def rule_promotion(sales, media):
    if sales < media:
        return "Need Promotion"
    else:
        return "Mantener"