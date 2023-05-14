### 데이터베이스에서 읽어오기
import pandas as pd
from sqlalchemy import create_engine  # 데이터베이스 사용 라이브러리
import pandas_datareader.data as web
import streamlit as st

username = st.secrets['DB']['username']
pw = st.secrets['DB']['pw']
address = st.secrets['DB']['address']
port = st.secrets['DB']['port']
schema = st.secrets['DB']['schema']


con = create_engine(f'mysql+pymysql://{username}:{pw}@{address}:{port}/{schema}')

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

### 재무 정보

def finance(code):
    df = pd.read_html(f'https://finance.naver.com/item/main.naver?code={code}',
                      encoding = 'cp949')
    finance_df = df[3]

    finance_df = finance_df.droplevel([0,2],axis=1)
    finance_df.index = finance_df.iloc[:,0]
    # finance_df = finance_df.drop('주요재무정보',axis=1)
    yearly = finance_df.iloc[:,:5]
    quarterly = finance_df.iloc[:,5:]
    
    return yearly, quarterly

def peer(code):
    df = pd.read_html(f'https://finance.naver.com/item/main.naver?code={code}',
                      encoding = 'cp949')
    peer_df = df[4]  # 경쟁사 정보  
    peer_df = peer_df.set_index('종목명') #인덱스 지정
    
    return peer_df
    
### 테스트
#df = finance('450140')

