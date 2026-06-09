import pandas as pd
import numpy as np
import os

np.random.seed(42)

product_category_map = {
    "Laptop": "Computers", "Smartphone": "Mobile", "Tablet": "Mobile",
    "Camera": "Accessories", "Headphones": "Audio", "Smartwatch": "Mobile",
    "Speaker": "Audio", "Monitor": "Computers", "Keyboard": "Accessories",
    "Mouse": "Accessories", "Printer": "Computers", "Router": "Accessories",
    "USB Hub": "Accessories", "Webcam": "Accessories", "Microphone": "Audio"
}

products = list(product_category_map.keys())

months = pd.date_range(start="2023-01-01", periods=12, freq='ME')

data = []

for month in months:
    for product in products:
        category = product_category_map[product]

        units = np.random.randint(50, 200)

        # Seasonal effect
        if month.month in [11, 12]:
            units *= 1.4
        elif month.month in [7, 8]:
            units *= 1.2
        elif month.month in [1, 2]:
            units *= 0.8
            
        units = int(units)

        price = np.random.uniform(1000, 80000)
        revenue = units * price

        discount = np.random.uniform(0, 0.15)
        net_revenue = revenue * (1 - discount)

        rating = np.random.uniform(3.5, 5.0)
        returns = int(units * np.random.uniform(0.01, 0.05))

        data.append([month.strftime("%Y-%m"), product, category, int(units),
                     price, revenue, discount, net_revenue, rating, returns])

df = pd.DataFrame(data, columns=[
    "Month", "Product", "Category", "Units_Sold", "Unit_Price",
    "Revenue", "Discount_Rate", "Net_Revenue",
    "Customer_Rating", "Returns"
])

os.makedirs("data", exist_ok=True)
df.to_csv("data/monthly_sales_data.csv", index=False)

print(" Data generated!")