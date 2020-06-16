import pandas as pd
result = pd.read_csv('C:\Users\ZhangYilun.CNSVWSH00\Desktop\L1\car_data_analyze\car_complain.csv',encoding='gbk')
print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)
tags = result.columns[7:]
#print(tags)

df= result.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉总数：')
print(df.sort_values('count', ascending=False))
df1= result.groupby(['brand','car_model'])['id'].agg(['count'])
print('车型投诉总数：')
print(df1.sort_values('count',ascending=False))
df2=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby( ['brand']).mean() 
print("平均投诉榜") 
print(df2.sort_values('count',ascending=False)) 
