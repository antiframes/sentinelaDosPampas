#juntar os ids dos deputados com os partidos
import pandas as pd
ids = pd.read_csv('depids.csv')
info = pd.read_csv('depinfo.csv')
res = pd.merge(ids,info,on='dep')
res.to_csv('2_prepared_data/deps.csv',index=False)
