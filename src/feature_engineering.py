import pandas as pd

def Load_dataset(path):
    return pd.read_csv(path)

df=Load_dataset(r"Data\cleaned_uber.csv")
print(df.head())         
        