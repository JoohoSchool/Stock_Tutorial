### 데이터베이스에서 읽어오기
import pandas as pd
from sqlalchemy import create_engine  # 데이터베이스 사용 라이브러리
import pandas_datareader.data as web

con = create_engine('mysql+pymysql://root:django@15.165.146.109:51126/stock')

### MySQL에서 가져오기
def info(code):  # 코드 입력 하면 정보가져오기
    query = f'''
            SELECT * FROM stock.info
            where 종목코드 = {code};
            '''
    print(query)
    df = pd.read_sql(query, con)
    return df

def info_name():  # 코드 입력 하면 정보가져오기
    query = '''
            SELECT 회사명, 종목코드 FROM stock.info
            order by 회사명
            '''
    print(query)
    df = pd.read_sql(query, con)
    return df

def info_name_code():  # 코드 입력 하면 정보가져오기
    query = '''
            SELECT 회사명, 종목코드 FROM stock.info
            order by 회사명
            '''
    print(query)
    df = pd.read_sql(query, con)
    
    return df['회사명'] + ' : ' + df['종목코드']

### 상장종목 리스트 가져오기
# pandas 데이터리더
# https://pydata.github.io/pandas-datareader/stable/index.html

# 상장기업 목록, 엑셀다운로드
# https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage
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

### 테스트
# info('005930')

