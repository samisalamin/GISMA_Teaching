
# Python Programming Course: Pandas Examples and Exercises

## Example 1: Creating Series and DataFrames
import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40])
print("Series:")
print(s)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

## Example 2: Filtering Data
# Filter rows where Age > 28
filtered_df = df[df['Age'] > 28]
print("\nFiltered DataFrame (Age > 28):")
print(filtered_df)

## Example 3: Grouping Data
# Add a new column for department
df['Department'] = ['HR', 'IT', 'HR']
grouped = df.groupby('Department').mean(numeric_only=True)
print("\nGrouped by Department:")
print(grouped)

## Example 4: Merging DataFrames
# Create another DataFrame
df2 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Salary': [50000, 60000]})
merged_df = pd.merge(df, df2, on='Name')
print("\nMerged DataFrame:")
print(merged_df)

## Example 5: Applying Functions
# Apply a function to calculate age in months
df['AgeInMonths'] = df['Age'].apply(lambda x: x * 12)
print("\nDataFrame with Age in Months:")
print(df)

# --- Self Exercises ---
# 1. Create a Series of 5 numbers and calculate their mean.
# 2. Create a DataFrame with columns 'Product', 'Price', 'Quantity' and calculate total value for each row.
# 3. Filter the DataFrame to show only rows where Quantity > 10.
# 4. Group the DataFrame by 'Product' and calculate the average price.
# 5. Merge two DataFrames: one with 'Employee' and 'Department', another with 'Employee' and 'Salary'.
# 6. Apply a function to a column to convert prices from USD to EUR (assume 1 USD = 0.85 EUR).
