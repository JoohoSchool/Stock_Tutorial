import pandas_datareader.data as web

import pandas as pd

import datetime as dt

df = web.DataReader('AAPL', 'yahoo')

df.head()