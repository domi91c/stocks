import csv
import datetime as dt
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

ANALYSIS_CSV_PATH = "./data/long_editors_picks_analysis.csv"
df = pd.read_csv("./data/long_editor_picks_04_01_21.csv")

analysis_data = {'stock': ['AAPL'], '0mth_price': [1], '3mth_price': [2],
                 '6mth_price': [3], '9mth_price': [4], '12mth_price': [5]}

analysis_df = pd.DataFrame(data=analysis_data)

print(analysis_data)
CSV_FILE = "./data/stock_pick_analysis.csv"
CSV_COLUMNS = ['stock', 'author',
               '0mth_price', '3mth_price', '6mth_price', '9mth_price', '12mth_price']


def ticker_history(stock, date, month_offset):
    print(stock)
    ticker = yf.Ticker(stock)
    end_date = dt.datetime.strptime(date, '%Y-%m-%d')
    end_date = end_date + relativedelta(months=6)
    ticker.history(start=date, end=end_date)


analysis_df['0mth_price'] = df.apply(
    lambda row: ticker_history(row['stock'], row['date'], 3), axis=1)
