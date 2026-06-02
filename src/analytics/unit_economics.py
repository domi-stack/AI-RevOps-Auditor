def cac(total_marketing_cost, new_customers):
    return total_marketing_cost / new_customers if new_customers > 0 else 0


def ltv(avg_revenue_per_customer, lifetime_months):
    return avg_revenue_per_customer * lifetime_months


def payback_period(cac_value, monthly_revenue_per_customer):
    return cac_value / monthly_revenue_per_customer if monthly_revenue_per_customer > 0 else 0


def unit_economics(marketing_cost, new_customers, avg_revenue, lifetime_months, monthly_revenue):
    cac_value = cac(marketing_cost, new_customers)
    ltv_value = ltv(avg_revenue, lifetime_months)
    payback = payback_period(cac_value, monthly_revenue)

    return {
        "CAC": round(cac_value, 2),
        "LTV": round(ltv_value, 2),
        "LTV_CAC_Ratio": round(ltv_value / cac_value, 2) if cac_value > 0 else 0,
        "Payback_Months": round(payback, 2)
    }
