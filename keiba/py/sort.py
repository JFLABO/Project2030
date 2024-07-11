import sys
import os
fl = sys.argv[1:]
print(fl[0])
import pandas as pd
#df = pd.read_csv('/home/net/query/202436062505.txt')
df = pd.read_csv(fl[0])
sorted_df = df.sort_values("os")
print(sorted_df)

#pandasで機械学習してオッズを軸に馬名称を並べ替えて表示しています
