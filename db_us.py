### 데이터베이스에서 읽어오기
import pandas as pd
from sqlalchemy import create_engine  # 데이터베이스 사용 라이브러리
import pandas_datareader.data as web
import streamlit as st
import yfinance as yf

username = st.secrets['DB']['username']
pw = st.secrets['DB']['pw']
address = st.secrets['DB']['address']
port = st.secrets['DB']['port']
schema = st.secrets['DB']['schema']

con = create_engine(f'mysql+pymysql://{username}:{pw}@{address}:{port}/{schema}')

def get_sp500_list():
    ''' 위키피디아에서 sp500 리스트 가져와서
        DB에 저장
    '''
    
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    sp500_companies = df[0]    
    sp500_companies.to_sql('sp500', con, if_exists = 'replace', index=False)
    print('sp500이 업데이트 되었습니다.')
    
def info(symbol):
    
    query = f'''
            select * from sp500
            where Symbol = "{symbol}"
            '''            
    print(query)
    df = pd.read_sql(query, con)
    return df
    
def info_name_code():
    
    query = f'''
            select Security, Symbol  from sp500
            '''            
    print(query)
    df = pd.read_sql(query, con)
    return df['Security'] + ' : ' + df['Symbol']

def us_stock(symbol):    
    ticker = yf.Ticker(symbol)
    df = ticker.history(period='3mo')
    return df
    
    