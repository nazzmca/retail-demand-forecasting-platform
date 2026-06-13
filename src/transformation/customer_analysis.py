import pandas as pd

INPUT_FILE = "data/processed/cleaned_retail_data.csv"
OUTPUT_FILE = "data/processed/customer_revenue.csv"

df = pd.read_csv(INPUT_FILE)

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

customer_revenue = (
    df.groupby("CustomerID")
    .agg(
        total_revenue=("Revenue", "sum"),
        total_orders=("InvoiceNo", "nunique"),
        total_items=("Quantity", "sum"),
    )
    .reset_index()
    .sort_values("total_revenue", ascending=False)
)

customer_revenue["average_order_value"] = (
    customer_revenue["total_revenue"] / customer_revenue["total_orders"]
)

customer_revenue.to_csv(OUTPUT_FILE, index=False)

print("\nCUSTOMER ANALYSIS SUMMARY")
print("=" * 50)
print(f"Total Customers: {customer_revenue['CustomerID'].nunique():,}")
print(f"Total Revenue: ${customer_revenue['total_revenue'].sum():,.2f}")

print("\nTop 10 Customers by Revenue")
print(customer_revenue.head(10))

print(f"\nCustomer revenue dataset saved to {OUTPUT_FILE}")