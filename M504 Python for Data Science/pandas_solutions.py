
# Solutions to Self Exercises

import pandas as pd

# 1. Create a Series of 5 numbers and calculate their mean.
s = pd.Series([5, 10, 15, 20, 25])
print("Mean of Series:", s.mean())

# 2. Create a DataFrame with columns 'Product', 'Price', 'Quantity' and calculate total value for each row.
df = pd.DataFrame({'Product': ['A', 'B', 'C'], 'Price': [10, 20, 15], 'Quantity': [5, 12, 8]})
df['TotalValue'] = df['Price'] * df['Quantity']
print("\nDataFrame with Total Value:")
print(df)

# 3. Filter the DataFrame to show only rows where Quantity > 10.
filtered_df = df[df['Quantity'] > 10]
print("\nFiltered DataFrame (Quantity > 10):")
print(filtered_df)

# 4. Group the DataFrame by 'Product' and calculate the average price.
grouped = df.groupby('Product').mean(numeric_only=True)
print("\nGrouped by Product (Average Price):")
print(grouped)

# 5. Merge two DataFrames: one with 'Employee' and 'Department', another with 'Employee' and 'Salary'.
df1 = pd.DataFrame({'Employee': ['John', 'Jane'], 'Department': ['HR', 'IT']})
df2 = pd.DataFrame({'Employee': ['John', 'Jane'], 'Salary': [70000, 80000]})
merged = pd.merge(df1, df2, on='Employee')
print("\nMerged DataFrame:")
print(merged)

# 6. Apply a function to a column to convert prices from USD to EUR (assume 1 USD = 0.85 EUR).
df['PriceEUR'] = df['Price'].apply(lambda x: round(x * 0.85, 2))
print("\nDataFrame with Price in EUR:")
print(df)
