import yfinance as yf
from datetime import datetime, date
import ta.momentum
import ta

def dfgenerator(ticker):
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = date(int(end_date[:4])-1, int(end_date[5:7]), int(end_date[9:]))


    # This try/except may seem weird but God knows how i tried to solve KeyError that just randomsly spanws sometimes due to YFinance
    # This way of doing it seems to solve it somehow
    try: 
        df = yf.download(ticker + ".SA", start = start_date, end = end_date)
    except KeyError:
        df = yf.download(ticker + ".SA", start = start_date, end = end_date)

    rolling_mean_period = 10
    deviations = 2

    df['deviation'] = df['Adj Close'].rolling(rolling_mean_period).std()
    df['RM'] = df['Adj Close'].rolling(rolling_mean_period).mean()
    df['Sup_Band'] = df['RM'] + (df['deviation'] * deviations)
    df['Inf_Band'] = df['RM'] - (df['deviation'] * deviations)

    df = df.dropna(axis = 0)

    df = getRSL(df)
    df = getRSI(df)

    return df

def getRSL(df):
    df['RSL'] = (df['Adj Close'] / df['RM'] - 1) * 100
    return df

def getRSI(df):
    stock_rsi = ta.momentum.RSIIndicator(close = df['Adj Close'], window = 10)
    df['RSI'] = stock_rsi.rsi()
    return df