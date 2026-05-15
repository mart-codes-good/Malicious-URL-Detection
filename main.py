# .venv\Scripts\Activate.ps1
import pandas as pd

# Read csv file and create a dataframe, run standard data cleaning operations
df = pd.read_csv('/kaggle/input/datasets/sid321axn/malicious-urls-dataset/malicious_phish.csv')

print("Number of null values:")
print(df.isnull().sum())

dupes = df.duplicated().sum()
print("Duplicates removed: ")
print(dupes)
df = df.drop_duplicates()

# print(df.head(10)) commented this line since the links are clickable on kaggle
