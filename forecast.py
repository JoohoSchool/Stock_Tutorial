from prophet import Prophet
import db

### 데이터 형식 맞추기
# https://facebook.github.io/prophet/docs/quick_start.html#python-api

### 주가예측
def forecast(code, start='2020-01-01', end=None, period = 30):
    price_df = db.korea_stock(code, start = start, end=end)   

    price_df['y'] = price_df['Close']
    price_df['ds'] = price_df.index
    
    df = price_df[['ds','y']]
    
    m = Prophet()  # prophet 모델 만들기
    m.fit(df)  # 학습하기
    
    future = m.make_future_dataframe(periods=period)  # 예측기간 설정
    
    forecast = m.predict(future)
    fig = m.plot(forecast)
    
    return fig

### 함수 테스트
# forecast('005930')