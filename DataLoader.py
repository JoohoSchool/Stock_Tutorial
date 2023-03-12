# pandas 데이터리더
# https://pydata.github.io/pandas-datareader/stable/index.html
import pandas_datareader.data as web


### DataReader Test
df = web.DataReader('065350', 'naver')  # 네이버 소스에서 데이터 불러오기
df.dtypes # 데이터 타입 확인

df = df.astype('int') # 정수로 변환
df.dtypes # 데이터 타입 확인

df['Close'].plot()  # 차트 그리기


# 데이터 불러오는 함수
def korea_stock(code, start, end):
    df = web.DataReader(code, 'naver', start=start, end=end)
    df = df.astype('int') # 정수로 변환
    return df

# 실행 스크립트
shinsung_df = korea_stock('065350', '2020-01-01', '2023-03-12')   
shinsung_df.Close.plot()
