import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r"Data\uber.csv")
print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFare Amount Statistics:")
print(df["fare_amount"].describe())

print("\nMinimum Fare:")
print(df["fare_amount"].min())
print("\nMaximum Fare:")

print(df["fare_amount"].max())
plt.figure(figsize=(8,5))

df["fare_amount"].hist(bins=50)
plt.title("Fare Amount Distribution")
plt.xlabel("Fare Amount")

plt.ylabel("Frequency")
plt.show()

#Here I removed 2 Colmns unnamed and key which doesnot require during my model evalution

df.drop(columns=["Unnamed: 0", "key"], inplace=True)

print(df.columns)

df.dropna(inplace=True)

print(df.isnull().sum())

print("Minimum Fare:")
print(df["fare_amount"].min())

df=df[df["fare_amount"]>0]
print("New Minimum Fare:")
print(df["fare_amount"].min())
df.to_csv("Data\\cleaned_uber.csv", index=False)
