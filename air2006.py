# 2006년의 출발지연 DepDelay / 도착지연ArrDelay 건수 조회

import pandas as pd

air2006 = pd.read_csv('/Users/yjm/Desktop/Java/2006.csv')

air2006.info()


# 출발지연DepDelay 건수
dd = air2006.loc[air2006['DepDelay'] > 0, :]
dd.DepDelay.head(10)
dd.groupby(['Year', 'Month'])['DepDelay'].count()

# 도착지연DepDelay 건수
dd = air2006.loc[air2006['ArrDelay'] > 0, :]
dd.ArrDelay.head(10)
dd.groupby(['Year', 'Month'])['ArrDelay'].count()
