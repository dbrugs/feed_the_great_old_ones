import yfinance as yf
import quandl
import numpy as np
import pandas as pd
from pandas import DataFrame

api_key = 'B6KP8sRUDocDsQw1zc8n'

def pull_symbol(symbol, source, start, end):
    if source == 'yahoo finance':
        data = yf.download(tickers = symbol, start = start, end = end)
        data['Symbol'] = symbol
        data['Date'] = data.index
        data.to_csv(symbol + '.csv')
    elif source == 'quandl':
        print('Enter Symbol Name:')
        data = quandl.get(dataset=symbol, start_date = start,end_date = end, api_key = api_key)
        data['Symbol'] = input()
        data['Date'] = data.index
        data.to_csv(symbol+'.csv')
    else:
        data = print('Its not here yet dude . . .')
    return data

def compute_price_data(Dataset, Price_input):
    #Date And Returns related computations
    Dataset['Date'] = Dataset.index
    Dataset['Day (Ordinal)'] = pd.DatetimeIndex(Dataset['Date']).dayofweek
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    Dataset['Day'] = Dataset['Day (Ordinal)'].apply(lambda x: weekdays[x])
    Dataset['Adj Close'] = Price_input
    Dataset['Prev_Close'] = Dataset.groupby(Dataset['Symbol'])['Adj Close'].shift(1)
    Dataset['Net Change'] = Dataset['Adj Close'] - Dataset['Prev_Close']
    Dataset['Net Change Percentage'] = Dataset['Net Change'].rank(pct = True)
    Dataset['Absolute Change'] = Dataset['Net Change'].abs()
    Dataset['Returns'] = (np.log(Dataset['Adj Close'] / Dataset['Prev_Close']))
    Dataset['Returns Percentage'] = Dataset['Returns'].rank(pct=True)
    Dataset['Year'] = pd.DatetimeIndex(Dataset['Date']).year
    Dataset['Prev_Close_Yrly'] = Dataset.groupby(['Symbol', 'Year'])['Adj Close'].shift(1)
    Dataset['quarter'] = pd.DatetimeIndex(Dataset['Date']).quarter
    Dataset['Previous_close_qrtr'] = Dataset.groupby(['Symbol', 'Year', 'quarter'])['Adj Close'].shift(1)
    Dataset['cum_returns'] = Dataset.groupby(['Symbol']).cumsum()['Returns']
    Dataset['Yrly_Returns'] = np.log(Dataset['Adj Close'] / Dataset['Prev_Close_Yrly'])
    Dataset['Qrtrly_Returns'] = np.log(Dataset['Adj Close'] / Dataset['Previous_close_qrtr'])


    ####VOL related computations
    Dataset['30 Day Vol'] = Dataset['Adj Close'].rolling(30).std()
    Dataset['30 Day Mean Vol'] = Dataset['30 Day Vol'].rolling(30).mean()
    Dataset['30 Day V Vol'] = Dataset['30 Day Vol'].rolling(30).std()
    Dataset['30 Day Vol z-score'] = Dataset['30 Day Vol'].pipe(lambda x: (x-x.mean())/x.std())
    Dataset['100 Day Vol'] = Dataset['Adj Close'].rolling(100).std()
    Dataset['100 Day Mean Vol'] = Dataset['100 Day Vol'].rolling(100).std()
    Dataset['100 Day V Vol'] = Dataset['30 Day Vol'].rolling(30).std()
    Dataset['100 Day Vol z-score'] = Dataset['100 Day Vol'].pipe(lambda x: (x - x.mean()) / x.std())

    ####technical indicators
    Dataset['SMA short'] = Dataset['Adj Close'].rolling(5).mean()
    Dataset['SMA mid'] = Dataset['Adj Close'].rolling(8).mean()
    Dataset['SMA long'] = Dataset['Adj Close'].rolling(15).mean()
    Dataset['200 Day SMA'] = Dataset['Adj Close'].rolling(200).mean()
    Dataset['50 Day SMA'] = Dataset['Adj Close'].rolling(50).mean()

    #Dataset['Position'] =
    #Dataset['Buy'] = x
    #Dataset['Sell'] = x
    #Dataset['Size'] =
    #Dataset.dropna(inplace=True)
    return Dataset

def grab_portfolio_data(investment_list, start, end):
    investments = {}
    i = 0
    for i in investment_list:
        investments[i] = i + '.txt'
    li = []
    for k, v in investments.items():
        try:
            df = yf.download(k, start, end)
            df['Symbol'] = k
            df.reset_index(inplace = True)
            li.append(df)
        except ValueError:
            print("Skipping"+ investment_list[i])
        portfolio = pd.concat(li, axis = 0, ignore_index=True)
        portfolio = DataFrame(portfolio)
    return portfolio
