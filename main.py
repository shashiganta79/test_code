import pandas as pd

produce = pd.read_csv("data/produce.csv")

print("Dataset Shape:")
print(produce.shape)

print("\nColumns:")
print(produce.columns)

print("\nFirst 5 Rows:")
print(produce.head())
print("\nStatistical Summary:")
print(produce.describe())
print("\nMissing Values:")
print(produce.isnull().sum())
# Fill only numeric columns with 0
numeric_cols = produce.select_dtypes(include='number').columns
produce[numeric_cols] = produce[numeric_cols].fillna(0)

print("\nMissing Values After Cleaning:")
print(produce.isnull().sum())
produce.to_csv("cleaned_produce.csv", index=False)
print("\nTop 10 Crop Categories:")
print(produce['Particulars'].head(10))
print("\nDataset Information:")
print(produce.info())

print("\nDataset saved successfully!")
print("\nTop 10 Crop Records:")
print(produce['Particulars'].head(10))