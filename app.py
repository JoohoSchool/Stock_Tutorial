import streamlit as st
import pandas as pd
import numpy as np
import db

st.title('Korean Stock Market')

code = st.text_input('Stock Code')
st.write('입력한 종목 코드는', code)

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
 