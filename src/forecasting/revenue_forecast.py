import pandas as pd
from sklearn.linear_model import LinearRegression

# Load monthly revenue
df = pd.read_csv("data/processed/monthly_revenue.csv")

# Create numeric month index
df["MonthIndex"] = range(len(df))

X = df[["MonthIndex"]]
y = df["Revenue"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Forecast next 3 months
future = pd.DataFrame({
    "MonthIndex": [13, 14, 15]
})

future["ForecastRevenue"] = model.predict(future)

# Save forecast
future.to_csv(
    "data/processed/revenue_forecast.csv",
    index=False
)

print("\nForecast Results")
print(future)

print("\nForecast saved to:")
print("data/processed/revenue_forecast.csv")