import pandas as pd

def calculate_answer(query):
    df = pd.read_csv("details.csv")
    query = query.lower()

    if "total profit" in query:
        return f"Total profit is {df['Profit'].sum()}"

    if "category" in query:
        return str(df.groupby("Category")["Profit"].sum())

    if "march" in query:
        return f"March profit is {df[df['Month']=='March']['Profit'].sum()}"

    return None