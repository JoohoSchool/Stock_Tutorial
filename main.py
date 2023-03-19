import DataLoader as dl

# 실행 스크립트
shinsung_df = dl.korea_stock('065350', '2020-01-01', '2023-03-12')   
shinsung_df.Close.plot()
