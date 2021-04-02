# import pdb
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mpl_dates
#
#
# from mpl_finance import candlestick_ohlc
#
#
#
#
#
# ohlc = hist.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
# ohlc['Date'] = pd.to_datetime(ohlc['Date'])
# ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
# ohlc = ohlc.astype(float)
#
# plt.show()

# import matplotlib.pyplot as plt
# import mplfinance as mpf
# import yfinance as yf
# import pandas as pd
# import matplotlib.dates as mpl_dates
#
# lspd = yf.Ticker("LUMN")
# hist = lspd.history(period="1wk", interval="60m", prepost=True)
#
# mpf.plot(hist, type='candle', mav=(3, 6, 9))

from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
