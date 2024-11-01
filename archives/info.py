import pandas as pd

df = pd.read_csv("survival.csv")

print(df.head())

print(df.info())

# PFS INFO
print("Minimum PFS: ", df['PFS_MONTHS'].min())
print(f"Median PFS: {df['PFS_MONTHS'].median()}")
print("Maximum PFS: ", df['PFS_MONTHS'].max())