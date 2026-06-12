import pandas as pd

df = pd.read_csv("data/processed/cleaned_retail_data.csv")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Revenue calculation
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Create Year-Month column
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

# Aggregate monthly revenue
monthly_revenue = (
    df.groupby("YearMonth")["Revenue"]
    .sum()
    .reset_index()
)

# Convert back to string for CSV
monthly_revenue["YearMonth"] = monthly_revenue["YearMonth"].astype(str)

# Save output
monthly_revenue.to_csv(
    "data/processed/monthly_revenue.csv",
    index=False
)

print(monthly_revenue)
print("\nRows:", len(monthly_revenue))