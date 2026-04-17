import pandas as pd
import os

df = pd.read_csv("data/monthly_sales_data.csv")
os.makedirs("outputs", exist_ok=True)

# Product stats
product_stats = df.groupby("Product").agg({
    "Units_Sold": "sum",
    "Net_Revenue": "sum",
    "Customer_Rating": "mean",
    "Returns": "sum"
}).reset_index()

product_stats.to_csv("outputs/product_statistics.csv", index=False)

# Category stats
category_stats = df.groupby("Category").agg({
    "Net_Revenue": "sum"
}).reset_index()

category_stats.to_csv("outputs/category_statistics.csv", index=False)

# Monthly trends
monthly = df.groupby("Month").agg({
    "Net_Revenue": "sum"
}).reset_index()

monthly.to_csv("outputs/monthly_trends.csv", index=False)

print("✅ Statistics done!")