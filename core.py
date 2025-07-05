# core.py
import yfinance as yf
import pandas_ta as ta
import datetime

def get_latest_data(ticker="AAPL", period="1d", interval="1m"):
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df

def apply_indicators(df):
    df["EMA_9"] = ta.ema(df["Close"], length=9)
    df["RSI"] = ta.rsi(df["Close"], length=14)
    df["Trend"] = df["Close"] > df["EMA_9"]
    return df

def signal(df):
    latest = df.iloc[-1]
    if latest["RSI"] < 30 and latest["Trend"]:
        return "BUY"
    elif latest["RSI"] > 70 and not latest["Trend"]:
        return "SELL"
    return "HOLD"

if __name__ == "__main__":
    data = get_latest_data()
    data = apply_indicators(data)
    print("Signal:", signal(data))
