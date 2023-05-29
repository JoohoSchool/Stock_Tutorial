import FinanceDataReader as fdr

# S&P 500 종목 전체
df_spx = fdr.StockListing('S&P500')
df_spx.head()


df = fdr.DataReader('AAPL', '2018-01-01', '2018-03-30')
df.tail()