import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_retail_data.csv")

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

country_revenue = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
country_revenue.plot(kind="bar")

plt.title("Top 10 Countries by Revenue")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("top_10_countries_revenue.png")

print("Chart saved: top_10_countries_revenue.png")