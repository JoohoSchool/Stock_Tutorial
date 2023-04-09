import DataLoader as dl
from sqlalchemy import create_engine
import pandas as pd

# Company Info 가져오기
kospi = dl.kospi_list()
kospi['거래소']='kospi'

kosdaq = dl.kosdaq_list()
kosdaq['거래소']='kosdaq'

result = pd.concat([kospi, kosdaq])

# DB 저장
con = create_engine('mysql+pymysql://root:django@13.125.114.237:54378/stock')

result.to_sql('info', con, if_exists = 'replace', index=False)

