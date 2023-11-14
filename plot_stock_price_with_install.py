import subprocess
import sys
from datetime import datetime

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Check for the availability of matplotlib and install if necessary
try:
    import matplotlib.pyplot as plt
except ImportError:
    install('matplotlib')
    import matplotlib.pyplot as plt

# Check for the availability of yfinance and install if necessary
try:
    import yfinance as yf
except ImportError:
    install('yfinance')
    import yfinance as yf

# Define the ticker symbol and the start date for YTD
ticker_symbol = 'AAPL' # Placeholder ticker symbol, replace with desired company's symbol
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