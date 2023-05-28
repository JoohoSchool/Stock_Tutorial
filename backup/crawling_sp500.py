# 위키피디아의 리스트 가져오기
# https://en.wikipedia.org/wiki/List_of_S%26P_500_companies


import pandas as pd


df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
sp500_companies = df[0]

# DB 저장
from sqlalchemy import create_engine
con = create_engine('mysql+pymysql://root:django@15.165.146.109:51126/stock')

sp500_companies.to_sql('sp500', con, if_exists = 'replace', index=False)
# 나오는 숫자는 rowcount임