from train import df
print(df["fare_amount"].describe())
df = df[df["fare_amount"] > 0]
print(df)