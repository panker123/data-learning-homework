# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:58:00 2020

@author: hp"""


import numpy as np
import pandas as pd
import pynlpir
from gensim.models import Word2Vec
import gensim
model_file = 'C:/Users/hp/Desktop/SentenceDistance-master/word2vec/news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=True)
#构建情感字典
def dict_create():
    file = pd.read_excel(r'C:\Users\hp\Desktop\情感词汇本体1.xlsx',encoding='ft')
    data2 = [] 
    file.fillna("", inplace=True)
    for i in file.index.values:
        df_line = file.loc[i, [ '情感分类', '情感强度', '情感极性','情感得分']].to_dict()
        data2.append(df_line)
    data1 = file['词语'].tolist()
    dictionary = dict(zip(data1, data2))    

    return dictionary

def similarity(sentence):
    topic1=pd.read_excel(r'C:\Users\hp\Desktop\苏州主题.xlsx',header=None)
    pynlpir.open()
    pynlpir.nlpir.ImportUserDict(b"C:\Users\hp\Desktop\mydic.txt")
    word=pynlpir.segment(sentence)
    d={}
    for i in range(topic1.shape[1]):
        s1=0
        for n in range(topic1.shape[0]):
            for n1 in range(len(word)):
                try:s1+=model.wv.similarity(word[n1][0],topic1[i][n])
                except:pass
        #print('分句与主题{}的相似的是{}'.format(i,s1/len(word)))
        d[i]=s1
    return max(zip(d.values(),d.keys()))

def items_create():

    text = pd.read_excel(r'C:\Users\hp\Desktop\分句2.xlsx', encoding='ft',index_col='D')
    topic = pd.read_excel(r'C:\Users\hp\Desktop\苏州主题.xlsx', encoding='ft', header=None)

    i_length = len(text.columns)  # 53
    j_length = len(topic.columns)  # 10

    i_i_length = len(text) #913
    j_j_length = len(topic) #11
    
    print(i_length,j_length,i_i_length,j_j_length)
#    print(text[911][1])
#    print(topic[1][3])
    #print(len(text.columns))
    
    #flag = [[1 for i in range(i_i_length)] for j in range(i_length)]
    f1=pd.DataFrame(np.ones((i_i_length,i_length)))
#    print(flag)
    '''for k in range(i_length): #k:文本横坐标
        for l in range(i_i_length):#l：文本纵坐标
            text[k][l] = str(text[k][l])
            if text[k][l]=='NAN':
                f1[k][l]=0
#            flag[k][l] = 1'''
    
    for k in range(j_length): #k:主题词横坐标
        for l in range(j_j_length): #l：主题词纵坐标
            topic[k][l] = str(topic[k][l])
            
         
    
    items = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    for kk in range(i_length):#kk:文本列数1
        for k in range(i_i_length):#k:文本行数913
            text_sentence=str(text.iloc[k])
            #print (k)
            for l in range(j_length):#l:主题数13
                for ll in range(j_j_length):
                    if(topic[l][ll]in text_sentence)and(f1[kk][k]==1):
                        items[l].append(text_sentence)
                        print(text_sentence)
                        f1[kk][k]=0
                        break
            if f1[kk][k]==1:
                sim=similarity(text_sentence)
                if sim[0]>0.5:
                    items[sim[1]].append(text_sentence)
        
    return items        
    
def score_add(sentence_list,dic):
    
    feeling = 0 #中性
    flag_set = 1
    result_list = []
    for word in sentence_list:        
        word = str(word)
        score = 0.0
        for key in dic.keys():
            key = str(key)
            if key in word and key != None and word !=None:

#                if key in ['inf', 'infinity', 'INF', 'INFINITY', 'True', 'NAN', 'nan', 'False', '-inf', '-INF', '-INFINITY', '-infinity', 'NaN', 'Nan']:
                try:
                    print(key)
                    print(sentence_list)
                    print(word)
                    print(dic[key]['情感得分'])
                    s = float(dic[key]['情感得分'])
                    score += s
                except:pass
        if score>0:
            feeling = 1
        elif score<0:
            feeling =-1
        result_list.append(word)
        result_list.append(feeling)
        result_list.append(score)
#        sentence_list.insert(flag_set , score)
#        sentence_list.insert(flag_set , feeling)
        flag_set += 3    
    return result_list

if __name__ == '__main__':
    items = items_create()        
    dictionary = dict_create()
    ggg = []
    aaa = []
    for item in items:
        aaa = score_add(item,dictionary)
        ggg.append(aaa)
    df = pd.DataFrame(ggg)
    df.to_excel(r'C:\Users\hp\Desktop\苏州情感2.xlsx', index=False)
