# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:49:02 2020

@author: hp
"""

import pandas as pd 
import numpy as np
sentence=pd.read_excel(r'C:\Users\hp\Desktop\主题情感得分2.xlsx')
text = pd.read_excel(r'C:\Users\hp\Desktop\精炼评论文本12.xlsx', encoding='ft',header=None)
t=np.full((912,30),np.nan)
t=pd.DataFrame(t)#构建存储矩阵
def get_sentence():#获得主题情感的分的每一个句子
    for k in range(sentence.shape[0]):
        print('归类主题{}'.format(k))
        s=sentence.loc[k].dropna()#获得k个主题下的所有句子和得分
        for i in range(0,len(s),3):
            a=s[i]#句子
            b=s[i+1]#极性
            c=s[i+2]#分数
            compare(a,b,c,k)
    
def compare(a,b,c,k):
    for l in range(text.shape[1]):
        for ll in range(text.shape[0]):#遍历文本
            if(text[l][ll]==a)and(c!=0):
                t[k*3][ll]=a
                t[k*3+1][ll]=b
                t[k*3+2][ll]=c
def main():
    get_sentence()
    t.to_excel(r'C:\Users\hp\Desktop\主题归类.xlsx')
main()