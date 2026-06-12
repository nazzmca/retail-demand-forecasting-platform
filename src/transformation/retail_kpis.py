import pandas as pd

df = pd.read_csv("data/processed/cleaned_retail_data.csv")

# Revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("\nRETAIL KPI SUMMARY")
print("=" * 50)

print(f"Total Revenue: ${df['Revenue'].sum():,.2f}")

print(f"Unique Customers: {df['CustomerID'].nunique():,}")

print(f"Unique Products: {df['StockCode'].nunique():,}")

print("\nTop 10 Countries by Revenue")

country_revenue = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(country_revenue.head(10))

print("\nTop 10 Products by Revenue")

product_revenue = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(product_revenue.head(10))