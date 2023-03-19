# pandas 데이터리더
# https://pydata.github.io/pandas-datareader/stable/index.html
import pandas_datareader.data as web

# 데이터 불러오는 함수
def korea_stock(code, start, end):
    df = web.DataReader(code, 'naver', start=start, end=end)
    df = df.astype('int') # 정수로 변환
    return df



