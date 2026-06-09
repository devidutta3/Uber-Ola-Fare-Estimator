import pandas as pd

df = pd.read_csv("Data\\uber.csv")

print(df.head())
print("\nDataset Info:")
df.info()

print("\nColumns:")
print(df.columns)
print("\n")
print("The Missing Values:\n")
print(df.isnull().sum())
print("\n")
print("The Duplicate Values:\n")
print(df.duplicated().sum())

df.drop(columns=["Unnamed: 0","key"],inplace=True)
df.dropna(inplace=True)

print("\n")
print(df.shape)