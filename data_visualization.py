import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/monthly_sales_data.csv")
os.makedirs("outputs", exist_ok=True)

# Monthly revenue
monthly = df.groupby("Month")["Net_Revenue"].sum()

plt.figure()
monthly.plot(marker='o')
plt.title("Monthly Revenue Trend")
plt.savefig("outputs/revenue_trend.png")

# Top products
top_products = df.groupby("Product")["Net_Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind='bar')
plt.title("Top Products")
plt.savefig("outputs/top_products.png")

print("✅ Charts created!")