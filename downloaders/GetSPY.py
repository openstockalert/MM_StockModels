import yfinance as yf

spy_data = yf.download('SPY', start='2015-01-02', end='2024-12-28')
spy_data = spy_data.drop(['High', 'Low', 'Volume'], axis=1)
spy_data = spy_data.round(2)
print(spy_data.head())

spy_data.to_csv("data/csv/spy_data.csv")