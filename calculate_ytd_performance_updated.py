import yfinance as yf
from datetime import datetime

# Define ticker symbols
meta_ticker = 'META'
tesla_ticker = 'TSLA'

# Get the start of the current year and today's date
tyda = datetime(datetime.today().year, 1, 1)
today = datetime.today().date()

# Fetch stock data for the YTD period
meta_data = yf.download(meta_ticker, start=tyda, end=today)
tesla_data = yf.download(tesla_ticker, start=tyda, end=today)

# Calculate YTD performance using iloc
meta_performance = ((meta_data['Close'].iloc[-1] - meta_data['Close'].iloc[0]) / meta_data['Close'].iloc[0]) * 100
tesla_performance = ((tesla_data['Close'].iloc[-1] - tesla_data['Close'].iloc[0]) / tesla_data['Close'].iloc[0]) * 100

# Print results
print(f'META YTD Performance: {meta_performance:.2f}%')
print(f'TESLA YTD Performance: {tesla_performance:.2f}%')
