import pandas as pd

def load_documents():
    df = pd.read_csv("details.csv")

    documents = []

    for _, row in df.iterrows():
        text = f"""
        Order {row['Order ID']}:
        Category: {row['Category']}
        Sub-Category: {row['Sub-Category']}
        Payment Mode: {row['PaymentMode']}
        Amount: {row['Amount']}
        Profit: {row['Profit']}
        Quantity: {row['Quantity']}
        """
        documents.append(text)

    return documents