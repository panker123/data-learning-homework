import pandas as pd
import numpy as np
text=pd.read_excel(r'C:\Users\hp\Desktop\峨眉山主题情感得分2.xlsx')
n=7#自然风光的行数
text_z=text.iloc[7].dropna()
ls=[]
for i in range (0,len(text_z),3):
    ls.append(text_z[i])
print(ls)
p1=pd.DataFrame(ls)
p1.to_excel(r'C:\Users\hp\Desktop\评论天气气候.xlsx')