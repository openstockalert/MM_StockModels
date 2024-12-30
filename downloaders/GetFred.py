import pandas_datareader.data as web
import datetime

start = datetime.datetime(2011, 1, 3)

sp500 = web.DataReader("SP500", "fred", start)
nasdaq = web.DataReader("NASDAQCOM", "fred", start)
dow = web.DataReader("DJIA", "fred", start)
vix = web.DataReader("VIXCLS", "fred", start)

vix = vix.dropna()
sp500 = sp500.dropna()
nasdaq = nasdaq.dropna()
dow = dow.dropna()



vix.to_csv("data/csv/data_vix.csv", decimal=".")
sp500.to_csv("data/csv/data_sp500.csv", decimal=".")
nasdaq.to_csv("data/csv/data_nasdaq.csv", decimal=".")
dow.to_csv("data/csv/data_dow.csv", decimal=".")