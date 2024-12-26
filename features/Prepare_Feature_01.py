import pandas as pd
import numpy as np

from Calculate_Featue import add_technical_indicators

# Load the data
# Replace 'your_file.csv' with your actual file path
file_path = 'data/csv/data_sp500_vix_fng.csv'
df = pd.read_csv(file_path, parse_dates=['DATE'])

# Ensure the data is sorted by date
df = df.sort_values('DATE').reset_index(drop=True)

df = add_technical_indicators(df)

# Create lag features for VIX and Fear and Greed Index (FNG)
# For example, create 1-day and 3-day lagged features
for lag in [1, 3, 5]:
    df[f'VIX_lag{lag}'] = df['VIX'].shift(lag)
    df[f'FNG_lag{lag}'] = df['FNG'].shift(lag)
    df[f'RSI_lag{lag}'] = df['RSI'].shift(lag)
    df[f'BB_Upper_Distance_lag{lag}'] = df['BB_Upper_Distance'].shift(lag)
    df[f'BB_Lower_Distance_lag{lag}'] = df['BB_Lower_Distance'].shift(lag)

# Create moving averages for VIX and FNG (optional for smoothing effects)
df['VIX_MA3'] = df['VIX'].rolling(window=3).mean().round(2)
df['FNG_MA3'] = df['FNG'].rolling(window=3).mean().round(2)

# Create target variables for next-day, 3-day, and 5-day predictions
# Binary target: 1 if the S&P 500 goes up, 0 if it goes down
df['S&P_1day_up'] = (df['SP500'].shift(-1) > df['SP500']).astype(int)
df['S&P_3day_up'] = (df['SP500'].shift(-3) > df['SP500']).astype(int)
df['S&P_5day_up'] = (df['SP500'].shift(-5) > df['SP500']).astype(int)

# Drop rows with missing values created by lagging or moving averages
df = df.dropna()

# Save the processed data to a new CSV file for modeling
output_file = 'features/processed_data/feature_data_01.csv'
df.to_csv(output_file, index=False)

print(f"Feature engineering complete. Processed data saved to '{output_file}'.")
