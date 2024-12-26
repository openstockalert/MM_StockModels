import pandas as pd

# Load the SP500 and VIX CSV files
sp500 = pd.read_csv('data/csv/data_sp500.csv')
vix = pd.read_csv('data/csv/data_vix.csv')
fng = pd.read_csv('data/csv/data_fearandgreed.csv')

# Merge the SP500 and VIX datasets on the date column
merged_sp500_vix = pd.merge(sp500, vix, on='DATE')

# Merge the merged_sp500_vix and FNG datasets on the date column
merged = pd.merge(merged_sp500_vix, fng, on='DATE')

# Save the merged dataset to a new CSV file
merged.to_csv('data/csv/data_sp500_vix_fng.csv', index=False)