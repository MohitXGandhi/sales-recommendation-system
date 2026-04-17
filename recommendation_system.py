import pandas as pd
import os

df = pd.read_csv("data/monthly_sales_data.csv")
os.makedirs("outputs", exist_ok=True)

product = df.groupby("Product").agg({
    "Units_Sold": "sum",
    "Net_Revenue": "sum",
    "Customer_Rating": "mean",
    "Returns": "sum"
}).reset_index()

# Normalize + Score
product["Score"] = (
    0.35 * (product["Net_Revenue"] / product["Net_Revenue"].max()) +
    0.30 * (product["Units_Sold"] / product["Units_Sold"].max()) +
    0.20 * (product["Customer_Rating"] / 5) +
    0.15 * (1 - product["Returns"] / product["Returns"].max())
)

product = product.sort_values(by="Score", ascending=False)

product.to_csv("outputs/ranked_products.csv", index=False)

print("✅ Ranking done!")