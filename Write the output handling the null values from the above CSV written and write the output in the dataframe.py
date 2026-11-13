import pandas as pd

# Read CSV file
df = pd.read_csv("employees.csv")

# Check NULL values
print(df.isnull().sum())

# Replace NULL values
df["department"] = df["department"].fillna("Unknown")
df["salary"] = df["salary"].fillna(0)

# Display cleaned DataFrame
print(df)