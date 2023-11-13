import pandas as pd
df = pd.read_csv('short_walk.csv')
df.head()
df = df.reindex(columns=['Time (s)','Accelerometer X (g)','Accelerometer Y (g)','Accelerometer Z (g)','Gyroscope X (deg/s)','Gyroscope Y (deg/s)','Gyroscope Z (deg/s)'])
#neworder = ['Time (s)','Accelerometer X (g)','Accelerometer Y (g)','Accelerometer Z (g)','Gyroscope X (deg/s)','Gyroscope Y (deg/s)','Gyroscope Z (deg/s)']#新的列顺序
#df = df.reindex(columns=neworder)
print(df)
df.to_csv("tag.csv",encoding='utf-8',index=False) # 在存csv的时候就避免这个问题，不要加索引, 否则第一列为行数。本文要求第一列为时间。
# 输出修改后的数据表
