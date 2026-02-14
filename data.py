import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\BMW sales data (2010-2024) (1).csv")

# -----------------------------
# Basic Exploration
# -----------------------------
print(df.head())
print(df.info())
print(df.describe())


# -----------------------------
# 1. Year-wise Total Sales
# -----------------------------
year_sales = df.groupby("Year")["Sales_Volume"].sum()

plt.figure()
plt.plot(year_sales.index, year_sales.values)
plt.xlabel("Year")
plt.ylabel("Total Sales Volume")
plt.title("BMW Total Sales Volume by Year")
plt.show()

# -----------------------------
# 2. Average Price by Fuel Type
# -----------------------------
fuel_price = df.groupby("Fuel_Type")["Price_USD"].mean()

plt.figure()
fuel_price.plot(kind="bar")
plt.xlabel("Fuel Type")
plt.ylabel("Average Price (USD)")
plt.title("Average BMW Price by Fuel Type")
plt.show()

# -----------------------------
# 3. Sales Volume by Region
# -----------------------------
region_sales = df.groupby("Region")["Sales_Volume"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.xlabel("Region")
plt.ylabel("Total Sales Volume")
plt.title("BMW Sales Volume by Region")
plt.show()

# -----------------------------
# 4. Mileage vs Price
# -----------------------------
plt.figure()
plt.scatter(df["Mileage_KM"], df["Price_USD"])
plt.xlabel("Mileage (KM)")
plt.ylabel("Price (USD)")
plt.title("Mileage vs Price")
plt.show()
