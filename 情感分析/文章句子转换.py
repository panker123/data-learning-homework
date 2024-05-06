import pandas as pd
import numpy as np
text=pd.read_excel(r'C:\Users\hp\Desktop\苏州1.xlsx')
print(text)
print(text.iloc[2])
print(len(text.iloc[2]))
ls=[]
for i in range(text.shape[0]):
    sentence=str(text.loc[i][0])
    #sentence=sentence.replace("\n\n",'。')
    t=''
    for j in sentence:
        t+=j
        if j in '?！？……。':
            print(t)
            ls.append(t)
            t=''
a=pd.DataFrame(ls)
print(a)
a.to_excel(r'C:\Users\hp\Desktop\苏州画像分句.xlsx')
