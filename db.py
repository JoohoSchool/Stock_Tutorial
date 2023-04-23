### 데이터베이스에서 읽어오기
import pandas as pd
from sqlalchemy import create_engine  # 데이터베이스 사용 라이브러리
import DataLoader as dl
from prophet import Prophet

con = create_engine('mysql+pymysql://root:django@13.125.114.237:54378/stock')

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

def info_name2():  # 코드 입력 하면 정보가져오기
    query = '''
            SELECT 회사명, 종목코드 FROM stock.info
            order by 회사명
            '''
    print(query)
    df = pd.read_sql(query, con)
    
    return df['회사명'] + ' : ' + df['종목코드']

def forecast(code, start='2020-01-01', end=None, period = 30):
    price_df = dl.korea_stock(code, start = start, end=end)
    
    ### 데이터 형식 맞추기
    # https://facebook.github.io/prophet/docs/quick_start.html#python-api
    
    price_df['y'] = price_df['Close']
    price_df['ds'] = price_df.index
    
    df = price_df[['ds','y']]
    
    m = Prophet()  # prophet 모델 만들기
    m.fit(df)  # 학습하기
    
    future = m.make_future_dataframe(periods=period)  # 예측기간 설정
    
    forecast = m.predict(future)
    fig = m.plot(forecast)
    
    return fig