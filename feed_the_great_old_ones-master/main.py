import functions as fn
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import numpy as np
import yfinance as yf
import pandas_datareader as web
api_key = 'B6KP8sRUDocDsQw1zc8n'
write_path = r'/home/brugs_bunny/scripts/viper_data'
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
start = datetime(2015,10,1)
end = datetime.today()
initial_capital = 1000000.00
#######################################################
#########################################################################
#INFLATIONARY COMMODITIES

    #oil
#quandl.get('CHRIS/ICE_T1', start_date = start, end_date = end, api_key = api_key)
oil = web.DataReader('CHRIS/ICE_T1' ,'quandl',  start, end, api_key = api_key)
oil['Symbol'] = 'CL'
    #oil weekly data
oil_weekly = DataFrame()
oil_weekly['Open'] = oil['Open'].resample('W').first()
oil_weekly['High'] = oil['High'].resample('W').max()
oil_weekly['Low'] = oil['Low'].resample('W').min()
oil_weekly['Settle'] = oil['Settle'].resample('W').last()
oil_weekly.to_csv(write_path+'oil_weekly.csv')
    #oil monthly data,
oil_monthly = DataFrame()
oil_monthly['Open'] = oil['Open'].resample('M').first()
oil_monthly['High'] = oil['High'].resample('M').max()
oil_monthly['Low'] = oil['Low'].resample('M').min()
oil_monthly['Settle'] = oil['Settle'].resample('M').last()
oil_monthly.to_csv(write_path+'oil_monthly.csv')
###############################################################
    #gold
gold = gold = web.DataReader('CHRIS/CME_GC1','quandl',  start, end, api_key = api_key)
gold['Symbol'] = 'GC'

    #gold weekly data
gold_weekly = DataFrame()
gold_weekly['Open'] = gold['Open'].resample('W').first()
gold_weekly['High'] = gold['High'].resample('W').max()
gold_weekly['Low'] = gold['Low'].resample('W').min()
gold_weekly['Settle'] = gold['Settle'].resample('W').last()
gold_weekly.to_csv(write_path+'gold_weekly.csv')
    #gold monthly data
gold_monthly = DataFrame()
gold_monthly['Open'] = gold['Open'].resample('M').first()
gold_monthly['High'] = gold['High'].resample('M').max()
gold_monthly['Low'] = gold['Low'].resample('M').min()
gold_monthly['Settle'] = gold['Settle'].resample('M').last()
gold_monthly.to_csv(write_path+'gold_monthly.csv')
############################################################################33
###########################################################################
#EQUITIES

    #NASDAQ
nsdq = web.DataReader('CHRIS/CME_NQ1' ,'quandl',  start, end, api_key = api_key)
nsdq['Symbol'] = 'NASDAQ'
    #nsdq weekly data
nsdq_weekly = DataFrame()
nsdq_weekly['Open'] = nsdq['Open'].resample('W').first()
nsdq_weekly['High'] = nsdq['High'].resample('W').max()
nsdq_weekly['Low'] = nsdq['Low'].resample('W').min()
nsdq_weekly['Settle'] = nsdq['Settle'].resample('W').last()
nsdq_weekly.to_csv(write_path+'nsdq_weekly.csv')
    #nsdq monthly data
nsdq_monthly = DataFrame()
nsdq_monthly['Open'] = nsdq['Open'].resample('M').first()
nsdq_monthly['High'] = nsdq['High'].resample('M').max()
nsdq_monthly['Low'] = nsdq['Low'].resample('M').min()
nsdq_monthly['Settle'] = nsdq['Settle'].resample('M').last()
nsdq_monthly.to_csv(write_path+'nsdq_monthly.csv')
#############################################################################################
    #SP500
es = web.DataReader('CHRIS/CME_ES1' ,'quandl',  start, end, api_key = api_key)
es['Symbol'] = 'SP500'
    #SP500 Weekly
es_weekly = DataFrame()
es_weekly['Open'] = es['Open'].resample('W').first()
es_weekly['High'] = es['High'].resample('W').max()
es_weekly['Low'] = es['Low'].resample('W').min()
es_weekly['Settle'] = es['Settle'].resample('W').last()
es_weekly.to_csv(write_path+'es_weekly.csv')
    #es monthly data
es_monthly = DataFrame()
es_monthly['Open'] = es['Open'].resample('M').first()
es_monthly['High'] = es['High'].resample('M').max()
es_monthly['Low'] = es['Low'].resample('M').min()
es_monthly['Settle'] = es['Settle'].resample('M').last()
es_monthly.to_csv(write_path+'es_monthly.csv')
###########################################################################33
#############################################################################3
#VOLATILITY
vix = yf.download('^VIX', start = start, end = end)
vix["Symbol"] = 'VIX'
vix.to_csv(write_path+'vix.csv')
    #vix weekly
vix_weekly = DataFrame()
vix_weekly['Open'] = vix['Open'].resample('W').first()
vix_weekly['High'] = vix['High'].resample('W').max()
vix_weekly['Low'] = vix['Low'].resample('W').min()
vix_weekly['Adj Close'] = vix['Adj Close'].resample('W').last()
vix_weekly.to_csv(write_path+'vix_weekly.csv')
    #vix monthly data
vix_monthly = DataFrame()
vix_monthly['Open'] = vix['Open'].resample('M').first()
vix_monthly['High'] = vix['High'].resample('M').max()
vix_monthly['Low'] = vix['Low'].resample('M').min()
vix_monthly['Adj Close'] = vix['Adj Close'].resample('M').last()
vix_monthly.to_csv(write_path+'vix_monthly.csv')
############################################################################

    #Curve Data VX1-VX5
vx1 = web.DataReader('CHRIS/CBOE_VX1' ,'quandl',  start, end, api_key = api_key)
vx1['Symbol'] = 'VX1'
vx1.to_csv(write_path+'vx1.csv')
#######################################################################
vx2 = web.DataReader('CHRIS/CBOE_VX2' ,'quandl',  start, end, api_key = api_key)
vx2['Symbol'] = 'VX2'
vx2.to_csv(write_path+'vx2.csv')
#######################################################################
vx3 = web.DataReader('CHRIS/CBOE_VX3' ,'quandl',  start, end, api_key = api_key)
vx3['Symbol'] = 'VX3'
vx3.to_csv(write_path+'vx3.csv')
#######################################################################
vx4 = web.DataReader('CHRIS/CBOE_VX4' ,'quandl',  start, end, api_key = api_key)
vx4['Symbol'] = 'VX4'
vx4.to_csv(write_path+'vx4.csv')
#######################################################################
vx5 = web.DataReader('CHRIS/CBOE_VX5' ,'quandl',  start, end, api_key = api_key)
vx5['Symbol'] = 'VX5'
vx5.to_csv(write_path+'vx5.csv')
#######################################################################
#######################################################################
#CURRENCIES
    #USD
dollar = web.DataReader('CHRIS/ICE_DX1' ,'quandl',  start, end, api_key = api_key)
dollar['Symbol'] = 'USD'
    #USD WEEKLY
dollar_weekly = DataFrame()
dollar_weekly['Open'] = dollar['Open'].resample('W').first()
dollar_weekly['High'] = dollar['High'].resample('W').max()
dollar_weekly['Low'] = dollar['Low'].resample('W').min()
dollar_weekly['Settle'] = dollar['Settle'].resample('W').last()
dollar_weekly.to_csv(write_path+'dollar_weekly.csv')
    #dollar monthly data
dollar_monthly = DataFrame()
dollar_monthly['Open'] = dollar['Open'].resample('M').first()
dollar_monthly['High'] = dollar['High'].resample('M').max()
dollar_monthly['Low'] = dollar['Low'].resample('M').min()
dollar_monthly['Settle'] = dollar['Settle'].resample('M').last()
dollar_monthly.to_csv(write_path+'dollar_monthly.csv')
#######################################################################
#######################################################################
#FIXED INCOME'FRED/DGS2'
two_year = web.DataReader('FRED/DGS2','quandl',  start, end, api_key = api_key)
two_year['Symbol'] = '2YR'
#######################################################################
ten_year = web.DataReader('FRED/DGS10','quandl',  start, end, api_key = api_key)
ten_year['Symbol'] = '10YR'
#######################################################################
#######################################################################
#ECONOMIC INDICATORS
unemployment = two_year = web.DataReader('FRED/UNEMPLOY','quandl',  start, end, api_key = api_key)
#######################################################################
#Turn into a dictionary of asset classes
assets = [oil,nsdq,es,dollar, two_year,ten_year,gold]
ticker = ['CL', 'NASDAQ', 'SP500','USD','2YR','10YR','GC']
price_input = [oil['Settle'],nsdq['Settle'], es['Settle'], dollar['Settle'], two_year['Value'],ten_year['Value'],
               gold['Settle']]


#Compute the price data
fn.compute_price_data(es, es['Settle'])
es['Day'] = es['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
es.to_csv(write_path+'sp500.csv')

fn.compute_price_data(oil, oil['Settle'])
#oil['Day'] = oil['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
oil.to_csv(write_path+'oil.csv')

fn.compute_price_data(dollar, dollar['Settle'])
#dollar['Day'] = dollar['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
dollar.to_csv(write_path+'USD.csv')

fn.compute_price_data(gold, gold['Settle'])
#gold['Day'] = gold['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
gold.to_csv(write_path+'gold.csv')

fn.compute_price_data(two_year, two_year['Value'])
#two_year['Day'] = two_year['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
two_year.to_csv(write_path+'2YR.csv')

fn.compute_price_data(ten_year, ten_year['Value'])
#ten_year['Day'] = ten_year['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
ten_year.to_csv(write_path+'10YR.csv')

fn.compute_price_data(nsdq, nsdq['Settle'])
#nsdq['Day'] = nsdq['Day (Ordinal)'].apply(lambda x: (weekdays[x]))
nsdq.to_csv(write_path+'nasdaq.csv')


##change portfolio and weights here. Initial capital is at the top
portfolio = ['VTI', 'TLT', 'GLD', 'VXX']
all_weather_portfolio_dict = {'Symbol': portfolio,
                         'weight':[0.60,0.27,0.05,0.08]}

all_weather_portfolio = DataFrame(all_weather_portfolio_dict)
all_weather_portfolio['Initial Value'] = all_weather_portfolio['weight'] * initial_capital
all_weather_portfolio.to_csv(write_path+ "all_weather_portfolio.csv")

#download portfolio data
portfolio_data = fn.grab_portfolio_data(portfolio, start,end)
#Track initial_investment for each symbol
#all_weather_portfolio['init_price'] = (portfolio_data[['Adj Close']].loc[(portfolio_data['Date'] == start)
 #                   & portfolio_data['Symbol'].isin(all_weather_portfolio['Symbol'])]).values
#dalio['init_price'] = (portfolio[['Adj Close']].loc[(portfolio['Date'] == start) & portfolio['Symbol'].isin(dalio['Symbol'])]).values

#Returns Data
portfolio_data['Prev_Close'] = portfolio_data.groupby(portfolio_data['Symbol'])['Adj Close'].shift(1)
portfolio_data['Daily Net Change'] = portfolio_data['Adj Close'] - portfolio_data['Prev_Close']
portfolio_data['Daily Return'] = (np.log(portfolio_data['Adj Close']/portfolio_data['Prev_Close']))
portfolio_data['Year'] = pd.DatetimeIndex(portfolio_data['Date']).year
portfolio_data['Quarter'] = pd.DatetimeIndex(portfolio_data['Date']).quarter
portfolio_data['Prev_Close_Qtr'] = portfolio_data.groupby(['Symbol', 'Year', 'Quarter'])['Adj Close'].shift(1)
portfolio_data['Prev_Close_Yrly'] = portfolio_data.groupby(['Symbol', 'Year'])['Adj Close'].shift(1)
portfolio_data['Qrtly_Returns'] = np.log(portfolio_data["Adj Close"]/portfolio_data['Prev_Close_Qtr'])
portfolio_data['Yrly_Returns'] = np.log(portfolio_data["Adj Close"]/portfolio_data['Prev_Close_Yrly'])
portfolio_data['Cumulative Returns'] = portfolio_data.groupby(['Symbol']).cumsum()['Daily Return']

#Set days of week
portfolio_data['Day (Ordinal)'] = pd.DatetimeIndex(portfolio_data['Date']).dayofweek
portfolio_data['Day'] = portfolio_data['Day (Ordinal)'].apply(lambda x: (weekdays[x]))

#write to csv
portfolio_data.to_csv(write_path+ 'portfolio.csv')