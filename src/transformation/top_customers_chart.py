import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/customer_revenue.csv")

top_customers = df.head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_customers["CustomerID"].astype(str),
    top_customers["total_revenue"]
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "docs/images/top_customers_revenue.png"
)

print(
    "Chart saved: docs/images/top_customers_revenue.png"
)