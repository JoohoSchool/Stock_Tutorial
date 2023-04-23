import pandas as pd
from prophet import Prophet
import DataLoader as dl

code =  '005930'
price_df = dl.korea_stock(code, '2020-01-01')

### 데이터 형식 맞추기
# https://facebook.github.io/prophet/docs/quick_start.html#python-api


price_df['y'] = price_df['Close']
price_df['ds'] = price_df.index

df = price_df[['ds','y']]

m = Prophet()  # prophet 모델 만들기
m.fit(df)  # 학습하기

future = m.make_future_dataframe(periods=30)  # 예측기간 설정
future.tail()  # 데이터프레임 뒤쪽부터 5개 보기

forecast = m.predict(future)
fig1 = m.plot(forecast)
