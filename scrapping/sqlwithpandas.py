from sklearn import datasets
boston = datasets.load_boston()

import pandas as pd
df = pd.DataFrame(boston['data'],columns=boston['feature_names'])

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
df.to_sql('boston_table', connect, if_exists='replace') # 테이블 내용을 업데이트 해줌 (추가X)
# df.to_sql('boston_table', connect, if_exists='append') # 계속 추가해서 테이블에 붙임

print(df)

connect.close()