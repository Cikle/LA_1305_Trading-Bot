import os
import ccxt
import pandas as pd
import numpy as np
import time
import logging

# Configure logging
logging.basicConfig(filename='trading_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Retrieve API keys from environment variables
api_key = 'mSMjUQk3t3WTDcssuYPE8Bj8zYq3PdGIW0w0yz13WnnGzqgohSrDeha7uvQmgjtb'
api_secret = 'JUdfVwDptdTslBHDSHBrFU7gl3MHg9LKiGCkwVtW9cpPb1U5yG5mL4FynwXPB9A2'

# Set up the Binance Futures exchange connection using ccxt
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'options': {
        'defaultType': 'future',  # Enable futures trading
    },
    'enableRateLimit': True,
    'adjustForTimeDifference': True,  # Automatically adjust for time difference
})

def set_leverage(symbol, leverage):
    try:
        exchange.set_leverage(leverage, symbol)
        logging.info(f"Leverage set to {leverage}x for {symbol}.")
        print(f"Leverage set to {leverage}x for {symbol}.")
    except Exception as e:
        logging.error(f"Error setting leverage: {e}")
        print(f"Error setting leverage: {e}")

def fetch_ohlcv(symbol, timeframe='1m', limit=500):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        print(f"Fetched OHLCV data for {symbol}.")
        return df
    except Exception as e:
        logging.error(f"Error fetching OHLCV data: {e}")
        print(f"Error fetching OHLCV data: {e}")
        return pd.DataFrame()

def moving_average_crossover_strategy(data, short_window=9, long_window=21):
    data['short_ema'] = data['close'].ewm(span=short_window, adjust=False).mean()
    data['long_ema'] = data['close'].ewm(span=long_window, adjust=False).mean()
    data['signal'] = 0
    data.loc[short_window:, 'signal'] = np.where(
        data.loc[short_window:, 'short_ema'] > data.loc[short_window:, 'long_ema'], 1, 0)
    data['position'] = data['signal'].diff()
    return data

def get_current_price(symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        print(f"Fetched current price for {symbol}: {ticker['last']}")
        return ticker['last']
    except Exception as e:
        logging.error(f"Error fetching current price: {e}")
        print(f"Error fetching current price: {e}")
        return None

def place_order(symbol, order_type, side, amount, price=None):
    try:
        if order_type == 'market':
            order = exchange.create_order(symbol, order_type, side, amount)
        elif order_type == 'limit':
            order = exchange.create_order(symbol, order_type, side, amount, price)
        logging.info(f"Order placed: {order}")
        print(f"Order placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        print(f"Error placing order: {e}")
        return None

def get_balance(asset):
    try:
        balance = exchange.fetch_balance()
        print(f"Fetched balance for {asset}: {balance['total'][asset]}")
        return balance['total'][asset]
    except Exception as e:
        logging.error(f"Error fetching balance: {e}")
        print(f"Error fetching balance: {e}")
        return None

def calculate_trade_amount(symbol, notional_value=5.5):
    price = get_current_price(symbol)
    if price:
        trade_amount = notional_value / price
        print(f"Calculated trade amount for {symbol}: {trade_amount}")
        return trade_amount
    return None

# Main trading loop
symbol = 'DOGE/USDT'
base_asset = 'DOGE'
quote_asset = 'USDT'
notional_value = 5.5  # Trade with 5.5 USDT
previous_candle_close = None

# Set leverage to 1 before starting trading
set_leverage(symbol, 1)

while True:
    try:
        data = fetch_ohlcv(symbol, timeframe='1m')
        if data.empty:
            logging.warning("No data fetched, skipping this iteration.")
            print("No data fetched, skipping this iteration.")
            time.sleep(60)
            continue

        latest_candle_close = data['timestamp'].iloc[-1]
        if previous_candle_close is None or latest_candle_close > previous_candle_close:
            print("New candle detected.")
            previous_candle_close = latest_candle_close

            data = moving_average_crossover_strategy(data, short_window=9, long_window=21)

            current_price = get_current_price(symbol)
            if current_price is None:
                logging.warning("Could not fetch current price, skipping this iteration.")
                print("Could not fetch current price, skipping this iteration.")
                time.sleep(60)
                continue
            logging.info(f"Current Price: {current_price}")

            trade_amount = calculate_trade_amount(symbol, notional_value)
            if trade_amount is None:
                logging.warning("Could not calculate trade amount, skipping this iteration.")
                print("Could not calculate trade amount, skipping this iteration.")
                time.sleep(60)
                continue
            logging.info(f"Trade Amount: {trade_amount} {base_asset}")

            # Check for buy signal
            if data['position'].iloc[-1] == 1:
                print("Buy signal detected.")
                usdt_balance = get_balance(quote_asset)
                if usdt_balance is not None and usdt_balance >= notional_value:
                    order = place_order(symbol, 'market', 'buy', trade_amount)
                    if order:
                        logging.info(f"Buy Order Placed: {order}")
                        print(f"Buy Order Placed: {order}")

            # Check for sell signal
            elif data['position'].iloc[-1] == -1:
                print("Sell signal detected.")
                doge_balance = get_balance(base_asset)
                if doge_balance is not None and doge_balance >= trade_amount:
                    order = place_order(symbol, 'market', 'sell', trade_amount)
                    if order:
                        logging.info(f"Sell Order Placed: {order}")
                        print(f"Sell Order Placed: {order}")
        else:
            print("Waiting for new candle to close.")

        time.sleep(60)  # Sleep for a minute before checking again
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        time.sleep(60)
