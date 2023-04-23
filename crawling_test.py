import pandas as pd

df = pd.read_html('https://finance.naver.com/item/main.naver?code=065350',
                  encoding = 'cp949')
finance_df = df[3]

# 연간_매출액 = finance_df.iloc[0,1:5]  
# 연간_영업이익 = finance_df.iloc[1,1:5]

yearly =  finance_df.iloc[:,:5]  # 연간 데이터 가져오기
yearly.index = finance_df.iloc[:,0] # 행인덱스 사용 지정
yearly.columns = range(5) # 컬럼명 새로 생성
yearly = yearly.drop(0, axis=1) # 0번째 컬럼 삭제
yearly.columns = [2020,2021,2022,2023] # 컬럼명 새로 넣기

print(yearly.loc['매출액',2020])  # 특정 요소 가져오기
print(yearly.loc['영업이익',2022])


### 분기 데이터 df 만들기
quaterly = finance_df.iloc[:,5:]



