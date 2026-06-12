import pandas as pd
import matplotlib.pyplot as plt

historical = pd.read_csv("data/processed/monthly_revenue.csv")
forecast = pd.read_csv("data/processed/revenue_forecast.csv")

forecast_months = ["2012-01", "2012-02", "2012-03"]

plt.figure(figsize=(12, 6))

plt.plot(
    historical["YearMonth"],
    historical["Revenue"],
    marker="o",
    label="Historical Revenue"
)

plt.plot(
    forecast_months,
    forecast["ForecastRevenue"],
    marker="o",
    linestyle="--",
    label="Forecast Revenue"
)

plt.title("Retail Revenue Forecast")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("docs/images/revenue_forecast.png")

print("Forecast chart saved: docs/images/revenue_forecast.png")