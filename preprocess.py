# coding=utf-8
import pandas as pd

obj = pd.read_csv("./data/Building_Permits.csv",low_memory=False)

attr=[]

for item in obj.columns:
    n = obj[item].value_counts()
    if n.count() < 100:
        attr.append(item)
        print item,n.count()


df = obj[attr]

df.to_csv("./test.csv",index=False,header=False)





