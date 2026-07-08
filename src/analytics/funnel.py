import pandas as pd

def funnel_conversion(df):
    stages = ["MQL", "SQL", "Opportunity", "Won"]

    results = {}

    for i in range(len(stages) - 1):
        current = stages[i]
        next_stage = stages[i + 1]

        current_count = len(df[df["stage"] == current])
        next_count = len(df[df["stage"] == next_stage])

        conversion = (next_count / current_count * 100) if current_count > 0 else 0

        results[f"{current}_to_{next_stage}"] = round(conversion, 2)

    return results
