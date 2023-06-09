


import pandas_datareader.data as web
import pandas as pd

# 데이터 불러오는 함수
def korea_stock(code, start, end=None):    
    df = pd.DataFrame()
    if end is None: # end = None 이면 실행
        df = web.DataReader(code, 'naver', start=start)
    else: # end에 입력이 있을 때 실행
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