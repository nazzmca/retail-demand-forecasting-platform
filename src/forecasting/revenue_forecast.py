import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/processed/monthly_revenue.csv")

# Create month index
df["MonthIndex"] = range(len(df))

X = df[["MonthIndex"]]
y = df["Revenue"]

model = LinearRegression()
model.fit(X, y)

# Forecast next 3 months
future = pd.DataFrame({
    "MonthIndex": [13, 14, 15]
})

future["ForecastRevenue"] = model.predict(future)

print("\nForecast Results")
print(future)