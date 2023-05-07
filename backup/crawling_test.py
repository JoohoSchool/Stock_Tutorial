import pandas as pd

df = pd.read_html('https://finance.naver.com/item/main.naver?code=065350',
                  encoding = 'cp949')
finance_df = df[3]  # 재무정보 선택

finance_df = finance_df.droplevel([0, 2], axis=1) # MultiIndex 불필요한 정보 삭제
finance_df.index = finance_df.iloc[:,0] # 행인덱스 사용 지정
finance_df = finance_df.drop('주요재무정보',axis=1) # 복사된 컬럼 삭제
yearly =  finance_df.iloc[:,:5]  # 연간 데이터 가져오기
quaterly = finance_df.iloc[:,5:]  # 분기 데이터 가져오기

print(yearly.loc['매출액', '2020.12'])

# 경쟁사 정보
peer_df = df[4]  # 재무정보 선택
peer_df = peer_df.set_index('종목명') #인덱스 지정

