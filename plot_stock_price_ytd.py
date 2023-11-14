import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define the ticker symbol and the start date for YTD
ticker_symbol = 'AAPL'
start_date = datetime(datetime.today().year, 1, 1)

# Fetch the historical data for the ticker
stock_data = yf.download(ticker_symbol, start=start_date)

# Plot the stock's closing prices
plt.figure(figsize=(10, 5))
plt.plot(stock_data.index, stock_data['Close'], label='Closing Price')
plt.title(f'{ticker_symbol} Stock Price YTD')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

# Save the figure
plt.savefig('stock_price_ytd.png')
plt.close()