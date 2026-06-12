import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/monthly_revenue.csv")

plt.figure(figsize=(10, 6))
plt.plot(df["YearMonth"], df["Revenue"], marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("docs/images/monthly_revenue_trend.png")

print("Chart saved: docs/images/monthly_revenue_trend.png")