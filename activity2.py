import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/dirty_cafe_sales.csv")

df.replace(to_replace=["UNKNOWN", "ERROR"], value=pd.NA, inplace=True)

df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors='coerce')
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors='coerce')

df.dropna(inplace=True)

print(df["Total Spent"].mean())

print(df[(df["Total Spent"] > 20) & (df["Quantity"] > 2)])

print(df[(df["Payment Method"] == "Credit Card") & (df["Location"] == "In-store")])

print(df.groupby("Item")["Total Spent"].sum())

print(df.sort_values(by="Total Spent", ascending=False).head(10))

print(df[df["Total Spent"] > 50].sort_values(by="Total Spent", ascending=False))

print(df.groupby("Payment Method")["Total Spent"].mean())

df.groupby("Item")["Total Spent"].sum().plot(kind="bar")
plt.title("Total Sales per Item")
plt.xlabel("Item")
plt.ylabel("Total Sales")
plt.show()

df["Payment Method"].value_counts().plot(kind="pie")
plt.title("Payment Methods Distribution")
plt.ylabel("")
plt.show()

df.groupby("Transaction Date")["Total Spent"].sum().plot(kind="line")
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

print(df.head())