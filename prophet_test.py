
import pandas as pd
from prophet import Prophet
import DataLoader as dl

code =  '005930'
price_df = dl.korea_stock(code, '2020-01-01', '2023-04-16')

price_df['y'] = price_df['Close']
price_df['ds'] = price_df.index

df = price_df[['ds','y']]

m = Prophet()  # prophet 모델 만들기
m.fit(df)  # 학습하기

future = m.make_future_dataframe(periods=30)  # 예측기간 설정
future.tail()

forecast = m.predict(future)
fig1 = m.plot(forecast)
