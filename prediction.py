import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_profit():
    df = pd.read_csv("details.csv")

    df['Index'] = range(len(df))

    X = df[['Index']]
    y = df['Profit']

    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict([[len(df)]])

    return f"Predicted next value profit: {int(pred[0])}"