import pandas as pd

# Load the dataset
df = pd.read_csv('netflix1.csv')

# Display the first few rows of the dataset with missing values
print(df.head())
print(df.info())  # To display the columns with missing values

df = pd.read_csv('laptopData.csv')

print(df.head())
print(df.info())  # To display the columns with missing values

duplicates = df[df.duplicated()]
print("Number of duplicate records:", duplicates.shape[0])
print(duplicates)