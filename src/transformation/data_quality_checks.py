import pandas as pd


df = pd.read_excel("data/sample/online_retail.xlsx")

print("\nDATA QUALITY REPORT")
print("=" * 50)

print(f"Total Records: {len(df):,}")

print(f"\nMissing Customer IDs: {df['CustomerID'].isna().sum():,}")

print(f"Missing Descriptions: {df['Description'].isna().sum():,}")

print(f"Duplicate Records: {df.duplicated().sum():,}")

print(f"Negative Quantities: {(df['Quantity'] < 0).sum():,}")

print(f"Negative Prices: {(df['UnitPrice'] < 0).sum():,}")