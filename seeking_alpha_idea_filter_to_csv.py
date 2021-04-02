"""
Parses an HTML file which I saved after listing all of the top picks on
Seeking Alpha's idea filter.
"""

import csv
import datetime as dt

from bs4 import BeautifulSoup

HTML_FILE = "./data/long_editor_picks_04_01_21.html"
CSV_FILE = "./data/long_editor_picks_04_01_21.csv"
CSV_COLUMNS = ['stock', 'date', 'author']

page = open(HTML_FILE)
html = BeautifulSoup(page.read(), "lxml")

descriptions = html.find_all('div', {'class': 'article-desc'})


def format_date(date):
    for date_format in ['%a, %b.  %d, %I:%M %p', '%b.  %d, %Y, %I:%M %p']:
        try:
            parsed_date = dt.datetime.strptime(date, date_format)
            # If no year is found, 1900 is set. Replace this with current year.
            if parsed_date.year == 1900:
                parsed_date = parsed_date.replace(year=dt.date.today().year)
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            pass


try:
    with open(CSV_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_COLUMNS)
        writer.writeheader()

        for desc in descriptions:
            stock = desc.find(sasource='pro_idea_filter_symbol').text
            author = desc.find(sasource='pro_idea_filter_author').text
            date = desc.find(text=True, recursive=False)
            date = format_date(date)

            print(stock)

            data = {
                'stock': stock,
                'author': author,
                'date': date,
            }

            writer.writerow(data)
except IOError:
    print("I/O error")
