import streamlit as st
import pandas as pd
import numpy as np
import db
import DataLoader as dl

st.title('Korean Stock Market')

code = st.text_input('Stock Code')
st.write('입력한 종목 코드는', code)

name_df = db.info_name2()

# 빈칸 한개 추가하는 것 나중에 추가
name = st.selectbox('회사명을 입력하세요. ',name_df)
st.write(name)

code = name.split(':')[1].replace(' ','')  
st.write(code)

price_df = dl.korea_stock(code, '2020-01-01', '2023-04-16')
st.line_chart(price_df['Close'])

fig = db.forecast(code)  # 예측 차트 생성
st.pyplot(fig)  # 차트 출력


if code!='':
    
    try: # 아래 실행
        df = db.info(code)  # 데이터 불러오기
    except: # 에러나면 여기
        st.write('잘못 입력했습니다.')
    else: # 에러 안나면 여기  
        if(len(df)==1):      # 값이 제대로 나온 경우
            st.subheader(df['회사명'][0])
            
        else:   # 종목이 검색 안 되는 경우
            st.write('없는 종목입니다. ')
 