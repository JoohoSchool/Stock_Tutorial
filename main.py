import DataLoader as dl


shinsung_df = dl.korea_stock('065350', '2020-01-01', '2023-03-12')
shinsung_df.Close.plot()

kospi = dl.kospi_list()
kosdaq = dl.kosdaq_list()

code = kospi['종목코드'][0]
dl.korea_stock(code, '2020-01-01', '2023-03-18')

kospi_list = []

for i in range(0,10):
    code = kospi['종목코드'][i]
    a = dl.korea_stock(code, '2020-01-01', '2023-03-18')
    kospi_list.append(a)
    
kosdaq_list = []

for r in range(0,10):
    code = kosdaq['종목코드'][r]
    b = dl.korea_stock(code, '2020-01-01', '2023-03-18')
    kosdaq_list.append(b)
    
    
# DB 저장

from sqlalchemy import create_engine
con = create_engine('mysql+pymysql://root:django@3.34.50.194:54621/stock')
kospi.to_sql('kospi',con, if_exists='replace')
kosdaq.to_sql('kosdaq', con, if_exists = 'replace')

# 신성델타테크 가격 정보 테이블에 넣기
df = dl.korea_stock('065350', '2020-01-01', '2023-03-18')
df.to_sql('ssdt', con, if_exists = 'replace')


# DB에서 읽기
import pandas as pd
query = 'SELECT 회사명, 종목코드 FROM stock.kospi;'
df = pd.read_sql(query, con)

