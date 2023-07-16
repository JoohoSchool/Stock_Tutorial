# 한 종목의 주가 받는 것을 함수로 만들기
# 데이터베이스 저장 kr_price

import pandas as pd
from sqlalchemy import create_engine  # 데이터베이스 사용 라이브러리
import pandas_datareader.data as web

con = create_engine(f'mysql+pymysql://root:django@15.165.146.109:51126/stock')

def download_price(code, start, end):
    df = web.DataReader(code, 'naver', start=start, end=end)
    df = df.astype('int') # 정수로 변환    
    
    df = df.reset_index() # 날짜를 일반 컬럼으로 변환
    df['code'] = code
    print(df)
    df.to_sql('korea_prices', con, if_exists = 'append', index=False)
    return df
    
# df = download_price('065350', '20230101', '20230708')


# info에서 종목코드 10개 가져와서
# 같은 테이블에 10개 종목 저장하기
# 이때 컬럼에 종목코드 추가, 날짜를 일반 컬럼(인덱스 아님)
# to_sql에 append 옵션을 사용

def get_codes(num_codes = 10):
    query = f'''SELECT 종목코드 FROM stock.info
            order by 상장일 
            limit {num_codes};'''
    df = pd.read_sql(query, con)
    return df['종목코드'].values

def multi_download(codes, start, end):
    for code in codes:
        print(code)
        download_price(code, start, end)
        
codes = get_codes()
multi_download(codes, '20230101', '20230707')     


# 수익률 계산
stock1 = download_price('065350', '20230101', '20230707')
rtn = stock1['Close'].iloc[-1]/stock1['Close'][0] - 1

# 1종목의 수익률 계산하는 거 함수로 만들기
def rtn(code, start, end):
    price = download_price(code, start, end)
    rtn = price['Close'].iloc[-1]/price['Close'][0] - 1
    return rtn

# 여러종목 수익률 계산하는 함수 만들기
def rtns(codes, start, end):
    code_rtns = {}
    for code in codes:
        print(code)
        수익률 =  rtn(code, start, end)
        code_rtns[code]=수익률
    return code_rtns

codes = get_codes()
period_rtns =  rtns(codes, '20230101', '20230707')   
print(period_rtns)

# 10개 종목 수익률 순서대로 출력





  



