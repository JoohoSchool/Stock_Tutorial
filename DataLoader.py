# pandas 데이터리더
# https://pydata.github.io/pandas-datareader/stable/index.html

# 상장기업 목록, 엑셀다운로드
# https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage


import pandas_datareader.data as web
import pandas as pd

# 데이터 불러오는 함수
def korea_stock(code, start, end):
    df = web.DataReader(code, 'naver', start=start, end=end)
    df = df.astype('int') # 정수로 변환
    return df

def kospi_list():
    kospi = pd.read_csv('data/KOSPI-20230319.csv', encoding = 'cp949',
                        dtype = {'종목코드':'str'})
    return kospi

def kosdaq_list():
    kosdaq = pd.read_csv('data/KOSDAQ-20230319.csv', encoding = 'cp949',
                         dtype = {'종목코드':'str'})
    return kosdaq