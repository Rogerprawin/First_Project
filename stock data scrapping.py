import yfinance as yf
from datetime import datetime

ticker = "AAPL"

from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Enter end date in yyyy/mm/dd format: ')

try:
    from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
    to_datetime = datetime.strptime(to_date, '%Y/%m/%d')
except ValueError as e:
    print(f"Error with date format: {e}")
    exit()

try:
    stock_data = yf.download(ticker, start=from_datetime, end=to_datetime)
    if not stock_data.empty:
        print("Data fetched successfully.")
        stock_data.to_csv('data.csv')
        print("Data saved to 'data.csv'.")
    else:
        print("No data found for the given date range.")
except Exception as e:
    print(f"An error occurred: {e}")
