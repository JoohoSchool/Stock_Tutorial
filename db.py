### 데이터베이스에서 읽어오기
import pandas as pd
from sqlalchemy import create_engine  # 데이터베이스 사용 라이브러리

con = create_engine('mysql+pymysql://root:django@13.125.114.237:54378/stock')

def info(code):  # 코드 입력 하면 정보가져오기
    query = f'''
            SELECT * FROM stock.info
            where 종목코드 = {code};
            '''
    print(query)
    df = pd.read_sql(query, con)
    return df

if __name__ == '__main__':  # 여기서 실행될 때
    pass