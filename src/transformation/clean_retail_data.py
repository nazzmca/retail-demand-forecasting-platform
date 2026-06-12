import pandas as pd


INPUT_FILE = "data/sample/online_retail.xlsx"
OUTPUT_FILE = "data/processed/cleaned_retail_data.csv"


df = pd.read_excel(INPUT_FILE)

print(f"Original Records: {len(df):,}")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing customer ids
df = df.dropna(subset=["CustomerID"])

# Remove returns / negative quantities
df = df[df["Quantity"] > 0]

# Remove negative prices
df = df[df["UnitPrice"] > 0]

print(f"Clean Records: {len(df):,}")

df.to_csv(OUTPUT_FILE, index=False)

print(f"Clean dataset saved to {OUTPUT_FILE}")