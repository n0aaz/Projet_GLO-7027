import pandas as pd

csv_path = 'data/CES19.csv'

data = pd.read_csv(csv_path)

print(data.head())
