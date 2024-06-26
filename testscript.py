import os
import ccxt

# Retrieve API keys from environment variables
api_key = 'mSMjUQk3t3WTDcssuYPE8Bj8zYq3PdGIW0w0yz13WnnGzqgohSrDeha7uvQmgjtb'
api_secret = 'JUdfVwDptdTslBHDSHBrFU7gl3MHg9LKiGCkwVtW9cpPb1U5yG5mL4FynwXPB9A2'

if not api_key or not api_secret:
    raise ValueError("API key and secret must be set")

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
        print(f"Leverage set to {leverage}x for {symbol}.")
    except Exception as e:
        print(f"Error setting leverage: {e}")

def get_min_trade_amount(symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        min_notional = 5.1  # Minimum notional value in USD for DOGE/USDT with buffer
        min_trade_amount = min_notional / ticker['last']
        return min_trade_amount
    except Exception as e:
        print(f"Error fetching minimum trade amount: {e}")
        return None

def test_binance_connection():
    try:
        # Fetch account balance
        balance = exchange.fetch_balance()
        print("Balance fetched successfully.")
        print(balance)

        # Set leverage for the trading pair to 1
        symbol = 'DOGE/USDT'
        leverage = 1  # No leverage
        set_leverage(symbol, leverage)

        # Calculate minimum trade amount
        min_trade_amount = get_min_trade_amount(symbol)
        if min_trade_amount is None:
            print("Could not determine minimum trade amount.")
            return

        print(f"Minimum trade amount for {symbol}: {min_trade_amount}")

        # Ensure the trade amount meets the $5 notional requirement
        ticker = exchange.fetch_ticker(symbol)
        min_trade_amount = max(min_trade_amount, 5.5 / ticker['last'])  # Added a small buffer

        # Test placing a buy order
        order_type = 'market'
        side = 'buy'

        print(f"Placing a test {side} order for {min_trade_amount} {symbol} with {leverage}x leverage...")
        buy_order = exchange.create_order(symbol, order_type, side, min_trade_amount)
        print("Buy order placed successfully.")
        print(buy_order)

        # Test placing a sell order
        side = 'sell'
        print(f"Placing a test {side} order for {min_trade_amount} {symbol} with {leverage}x leverage...")
        sell_order = exchange.create_order(symbol, order_type, side, min_trade_amount)
        print("Sell order placed successfully.")
        print(sell_order)

    except ccxt.BaseError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_binance_connection()