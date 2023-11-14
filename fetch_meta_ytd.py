import yfinance as yf
from datetime import datetime

# Define the current year
current_year = datetime.now().year

# Define the stock symbol for Meta Platforms, Inc.
symbol = 'META'

# Fetch the historical data for META from the start of the year until today
data = yf.download(symbol, start=f'{current_year}-01-01', end=datetime.now().strftime('%Y-%m-%d'))

# Calculate the year-to-date (YTD) performance
start_price = data['Open'].iloc[0]
current_price = data['Close'].iloc[-1]
percentage_change = ((current_price - start_price) / start_price) * 100

# Output the YTD performance
print(f'META YTD Percentage Change: {percentage_change:.2f}%')
